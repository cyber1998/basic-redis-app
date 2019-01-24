import click
import logging

from flask import Flask
from redis import Redis
from rq import Queue, Worker, Connection
from logging.config import dictConfig

from app.models import db


# Redis Queue stuff
# Redis queue initialization

redis_connection = Redis()
queue = Queue('default', connection=redis_connection)

listen = ['default']


@click.command('worker')
def edyst_worker():
    with Connection(redis_connection):
        worker = Worker(map(Queue, listen))
        worker.work()


def create_app(config_module='app.configs.config'):
    from app.configs.config import APP_NAME

    # Setting up the app object
    app = Flask(APP_NAME)

    # Import app specific configuration
    app.config.from_object(config_module)

    # Initializing the root logger
    dictConfig(app.config['LOGGING'])
    logger = logging.getLogger(__name__)
    logger.debug('Logger initialized')

    db.init_app(app)

    from app.utilities import rebuild

    # Add the commands to the flask cli
    app.cli.add_command(rebuild)
    app.cli.add_command(edyst_worker)

    # Register the blueprint here
    from app.routes import generic_blueprint
    app.register_blueprint(generic_blueprint)
    return app

