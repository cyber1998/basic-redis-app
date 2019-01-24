import time
from flask import (
    request,
    render_template,
    Blueprint,
    redirect,
    url_for,
    flash
)

from app import queue
from app.models.webpages import Webpage
from app.tasks import count_words_at_url

generic_blueprint = Blueprint(
    'generic',
    __name__,
    template_folder='templates'
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
        job = queue.enqueue(count_words_at_url, data)
        time.sleep(2)

        # For demo purposes we use
        if job.result is True:
            flash('Here are your results')
            return redirect(url_for('generic.index'))
        flash('Bad url format. Please provide the full URL.'
              ' Example: http://google.com')
        return redirect(url_for('generic.index'))
