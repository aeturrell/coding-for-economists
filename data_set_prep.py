import pandas as pd
import os
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


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


if __name__ == '__main__':
    star_wars_data()
    save_smith_book()
