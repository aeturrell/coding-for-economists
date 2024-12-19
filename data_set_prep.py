import os
import urllib.request
from pathlib import Path

import geopandas as gpd
import pandas as pd
import shapely.geometry
from bs4 import BeautifulSoup
from bs4.element import Comment
from skimpy import clean_columns


def star_wars_data():
    """Saves star wars character data with set
    datatypes and in pickle format.
    """
    df = pd.read_csv(
        os.path.join("data", "characters.csv"),
        thousands=",",
        dtype={
            "name": "string",
            "height": float,
            "mass": float,
            "hair_color": "category",
            "skin_color": "category",
            "eye_color": "category",
            "birth_year": "string",
            "gender": "category",
            "homeworld": "category",
            "species": "category",
        },
    )
    df = df.drop(["skin_color", "birth_year"], axis=1)
    df.info()
    df.to_csv(os.path.join("data", "starwars.csv"))


def tag_visible(element):
    if element.parent.name in [
        "style",
        "script",
        "head",
        "title",
        "meta",
        "[document]",
    ]:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, "html.parser")
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return " ".join(t.strip() for t in visible_texts)


def save_smith_book():
    """Downloads part of the 'The Wealth of Nations' and saves it."""
    html = urllib.request.urlopen(
        "https://www.gutenberg.org/files/3300/3300-h/3300-h.htm"
    ).read()
    # Take the book text only
    book_text = (
        text_from_html(html)
        .split("Produced by Colin Muir, and David Widger")[1]
        .split("Conclusion of the Chapter.")[0]
    )
    print(book_text.split("\n")[0])
    open(os.path.join("data", "smith_won.txt"), "w").write(book_text)


def prep_river_data():
    """
    Download the 10m rivers, lakes, and centerlines from and put in scratch/rivers/
    https://www.naturalearthdata.com/downloads/10m-physical-vectors/10m-rivers-lake-centerlines/
    TODO: automate download of shapefile
    """
    rivers = gpd.read_file(
        os.path.join("scratch", "rivers", "ne_10m_rivers_lake_centerlines.shp")
    )
    uk_bound_box = (-7.57216793459, 49.959999905, 1.68153079591, 58.6350001085)
    uk_polygon = shapely.geometry.box(*uk_bound_box, ccw=True)
    rivers = rivers[rivers.within(uk_polygon)]
    rivers.to_file(os.path.join("data", "geo", "rivers", "rivers.shp"))


def prep_covid_data():
    """
    Downloads covid data from uk gov't website and processes it ready for plotting.
    """
    # data_url = "https://api.coronavirus.data.gov.uk/v2/data?areaType=ltla&metric=newDeaths28DaysByDeathDate&format=csv&release=2021-02-27"
    cv_df = pd.read_csv(os.path.join("~", "Downloads", "ltla_2021-02-27.csv"))
    cv_df["date"] = pd.to_datetime(cv_df["date"])
    cv_df["newDeaths28DaysByDeathDate"] = cv_df["newDeaths28DaysByDeathDate"].astype(
        int
    )
    cv_df["areaCode"] = cv_df["areaCode"].astype("string")
    cv_df["areaName"] = cv_df["areaName"].astype("string")
    cv_df = cv_df.rename(columns={"areaCode": "LAD20CD", "areaName": "LAD20NM"})
    cv_df = cv_df[cv_df["LAD20CD"].str.contains("E09")]
    cv_df = (
        cv_df.set_index(["date"])
        .groupby([pd.Grouper(freq="M"), "LAD20CD", "LAD20NM"])
        .sum()
        .reset_index()
    )
    cv_df.to_parquet(os.path.join("data", "geo", "cv_ldn_deaths.parquet"))


def prep_gapminder_data():
    """
    Downloaded from Our World in Data:
    https://ourworldindata.org/grapher/life-expectancy-vs-gdp-per-capita
    """
    df = pd.read_csv(
        os.path.join("~", "Downloads", "life-expectancy-vs-gdp-per-capita.csv")
    )
    df = df[df["Year"] > 1957]
    df = df.dropna(
        subset=[
            "Life expectancy",
            "GDP per capita",
            "Total population (Gapminder, HYDE & UN)",
        ]
    )
    continents_dict = (
        df.loc[df["Year"] == 2015, ["Entity", "Continent"]]
        .set_index("Entity")
        .to_dict()["Continent"]
    )
    df["Continent"] = df["Entity"].map(continents_dict)
    nice_names = {
        "Entity": "Country",
        "Total population (Gapminder, HYDE & UN)": "Population",
    }
    df = df.rename(columns=nice_names)
    df = df.drop(["Code", "145446-annotations"], axis=1)
    df = df[df["Country"] != "World"]
    df.to_csv(Path("data/owid_gapminder.csv"), index=False)


def prep_air_quality_data():
    # first download data from Air Quality Historical Data Platform
    df = pd.read_csv(Path("/Users/aet/Downloads/beijing-air-quality.csv"))
    df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")
    df = df.set_index("date")
    df = df.sort_index()
    # make 7 day rolling
    df = df.rolling(7).mean()
    df.to_csv(Path("data/beijing_pm.csv"))


def create_smaller_cut_flights_data():
    url = "https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/flights/flights.csv"
    flights = pd.read_csv(url)
    flights["time_hour"] = pd.to_datetime(flights["time_hour"])
    in_cols = ["year", "month", "day", "flight", "minute", "distance", "hour"]
    for col in in_cols:
        flights[col] = flights[col].astype("int")
    cat_cols = ["carrier", "tailnum", "origin", "dest"]
    for col in cat_cols:
        flights[col] = flights[col].astype("category")
    num_cols = [
        "dep_time",
        "sched_dep_time",
        "dep_delay",
        "arr_time",
        "arr_delay",
        "air_time",
    ]
    for col in num_cols:
        flights[col] = flights[col].astype("float")
    flights.sample(100000, random_state=78557).to_parquet("data/flights.parquet")


def prep_kaggle_data_on_tfl_trips():
    """Prep a sliver of Kaggle data on tfl trips for the tables page.
    Note that this uses data from this url: https://www.kaggle.com/code/benivitai/tfl-oyster-card-journeys-analysis
    This function expects that the csv file, Nov09JnyExport.csv, has been extracted and downloaded
    to data/data_not_stored/
    """

    tfl = pd.read_csv(Path("data/data_not_stored/Nov09JnyExport.csv"))
    tfl = clean_columns(tfl)
    # cast columns
    data_type_dict = {
        "downo": "int",
        "daytype": "category",
        "sub_system": "category",
        "start_stn": "category",
        "end_station": "category",
        "ent_time": "int",
        "ex_time": "int",
        "final_product": "category",
    }
    better_names_dict = {
        "downo": "dayofweek_num",
        "daytype": "day",
        "sub_system": "mode",
        "ent_time": "ent_mins_post_midnight",
        "ex_time": "ex_time_mins_post_midnight",
        "final_product": "pay_method",
    }
    names_to_remove = [x for x in tfl.columns if x not in data_type_dict.keys()]
    tfl = tfl.drop(names_to_remove, axis=1)
    tfl = tfl.astype(data_type_dict)
    tfl = tfl.rename(columns=better_names_dict)
    # filter out all bus journeys
    tfl = tfl.loc[~tfl["mode"] != "LTB", :]
    # filter all unstarted journeys (no start station)
    tfl = tfl.loc[tfl["start_stn"] != "Unstarted", :]
    tfl = tfl.sample(frac=0.1, random_state=4434)
    tfl.to_parquet(Path("data/tfl_small.parquet"))


if __name__ == "__main__":
    prep_river_data()
    star_wars_data()
    save_smith_book()
    prep_gapminder_data()
    prep_kaggle_data_on_tfl_trips()
