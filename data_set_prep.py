import pandas as pd
import os


def star_wars_data():
    """ Saves star wars character data with set
        datatypes and in feather format.
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

    df.info()
    df.to_feather(os.path.join('data', 'starwars.feather'))


star_wars_data()
