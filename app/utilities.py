import click
from flask.cli import with_appcontext
from app.models import db


@click.command('rebuild')
@with_appcontext
def rebuild():
    from app.models.webpages import Webpage
    db.drop_all()
    db.create_all()

