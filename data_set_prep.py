import pandas as pd
import os


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


star_wars_data()
