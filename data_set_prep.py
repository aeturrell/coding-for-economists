import pandas as pd
import os
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import geopandas as gpd
import shapely.geometry


def star_wars_data():
    """ Saves star wars character data with set
        datatypes and in pickle format.
    """
    df = pd.read_csv(os.path.join('data', 'characters.csv'),
                     thousands=',',
                     dtype={'name': 'string',
                            'height': float,
                            'mass': float,
                            'hair_color': 'category',
                            'skin_color': 'category',
                            'eye_color': 'category',
                            'birth_year': 'string',
                            'gender': 'category',
                            'homeworld': 'category',
                            'species': 'category'})
    df = df.drop(['skin_color', 'birth_year'], axis=1)
    df.info()
    df.to_pickle(os.path.join('data', 'starwars.pickle'))


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


def save_smith_book():
    """Downloads part of the 'The Wealth of Nations' and saves it."""
    html = (urllib
            .request
            .urlopen('https://www.gutenberg.org/files/3300/3300-h/3300-h.htm')
            .read())
    # Take the book text only
    book_text = (text_from_html(html)
                 .split('Produced by Colin Muir, and David Widger')[1]
                 .split('Conclusion of the Chapter.')[0])
    print(book_text.split('\n')[0])
    open(os.path.join('data', 'smith_won.txt'), 'w').write(book_text)


def prep_river_data():
    """
    Download the 10m rivers, lakes, and centerlines from and put in scratch/rivers/
    https://www.naturalearthdata.com/downloads/10m-physical-vectors/10m-rivers-lake-centerlines/
    TODO: automate download of shapefile
    """
    rivers = gpd.read_file(os.path.join('scratch', 'rivers', 'ne_10m_rivers_lake_centerlines.shp'))
    uk_bound_box = (-7.57216793459, 49.959999905, 1.68153079591, 58.6350001085)
    uk_polygon = shapely.geometry.box(*uk_bound_box, ccw=True)
    rivers = rivers[rivers.within(uk_polygon)]
    rivers.to_file(os.path.join('data', 'geo', 'rivers', 'rivers.shp'))


def prep_covid_data():
    """
    Downloads covid data from uk gov't website and processes it ready for plotting.
    """
    # data_url = "https://api.coronavirus.data.gov.uk/v2/data?areaType=ltla&metric=newDeaths28DaysByDeathDate&format=csv&release=2021-02-27"
    cv_df = pd.read_csv(os.path.join('~', 'Downloads', 'ltla_2021-02-27.csv'))
    cv_df['date'] = pd.to_datetime(cv_df['date'])
    cv_df['newDeaths28DaysByDeathDate'] = cv_df['newDeaths28DaysByDeathDate'].astype(int)
    cv_df['areaCode'] = cv_df['areaCode'].astype('string')
    cv_df['areaName'] = cv_df['areaName'].astype('string')
    cv_df = cv_df.rename(columns={'areaCode': 'LAD20CD', 'areaName': 'LAD20NM'})
    cv_df = cv_df[cv_df['LAD20CD'].str.contains('E09')]
    cv_df = cv_df.set_index(['date']).groupby([pd.Grouper(freq='M'), 'LAD20CD', 'LAD20NM']).sum().reset_index()
    cv_df.to_parquet(os.path.join('data', 'geo', 'cv_ldn_deaths.parquet'))


if __name__ == '__main__':
    prep_river_data()
    star_wars_data()
    save_smith_book()
