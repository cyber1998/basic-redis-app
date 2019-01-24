import logging

import bs4
import requests
from flask.cli import with_appcontext

from app.models import db
from app.models.webpages import Webpage

logger = logging.getLogger(__name__)


@with_appcontext
def count_words_at_url(data):
    """
    This is the worker function which will make a request to the
    web page and return the amount of words present in it.

    :param dict data: Contains the url of the site.
    """
    logger.info('Making a request to the URL...')
    resp = requests.get(data['url'])

    crawled = bs4.BeautifulSoup(resp.content)
    data = {
        'url': data['url'],
        'words': len(crawled.text.split()),
        'title': crawled.title.text
    }
    try:
        webpage = Webpage(data)
    except requests.exceptions.MissingSchema:
        logger.error('Failed to fetch data...'
                     'Please check the structure of the URL')
        return False
    except requests.exceptions.InvalidURL:
        logger.error('Failed to fetch data...'
                     'Please check the structure of the URL')
        return False
    except requests.exceptions.InvalidSchema:
        logger.error('Failed to fetch data...'
                     'Please check the structure of the URL')
        return False

    db.session.add(webpage)
    db.session.commit()

    return True
