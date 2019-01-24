import logging
import time

from flask import (
    request,
    render_template,
    Blueprint,
    redirect,
    url_for,
    abort
)

from app import queue
from app.models.webpages import Webpage
from app.tasks import count_words_at_url

logger = logging.getLogger(__name__)

generic_blueprint = Blueprint(
    'generic',
    __name__,
    template_folder='templates',
    static_url_path='../static'
)


@generic_blueprint.route('/')
@generic_blueprint.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        results = Webpage.get_all_details()
        return render_template('index.html', results=results)

    if request.method == 'POST':
        url = request.form.get('url')
        data = dict()
        data['url'] = url
        logger.info('Queing new job with url: {}'.format(url))

        # Queue a job
        job = queue.enqueue(count_words_at_url, data,)
        logger.info('Job id: {} has been queued'.format(job.get_id()))

        # Not waiting would result in the job getting queued and
        # successfully but committed to the database but the job result
        # will be a None type

        time.sleep(3)

        if job.result is True:
            logger.info('Job successful')
            return redirect(url_for('generic.index'), code=302)
        logger.error('Job unsuccessful')
        abort(400)
