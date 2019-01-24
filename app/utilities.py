import click
import logging

from flask.cli import with_appcontext
from app.models import db

logger = logging.getLogger(__name__)


@click.command('rebuild')
@with_appcontext
def rebuild():
    logger.debug('Recreating all tables and deleting all data...')
    from app.models.webpages import Webpage
    db.drop_all()
    db.create_all()


def test_rebuild():
    logger.debug('Rebuilding database for testing purposes..')
    from app.models.webpages import Webpage
    db.drop_all()
    db.create_all()
