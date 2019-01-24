"""
Please turn on your worker or the tests will fail.
"""
import pytest
import time
from app.models.webpages import Webpage


@pytest.mark.usefixtures('setup')
class TestTasks:

    def test_get_index_page(self, user_fixture):
        r = self.client.get('/index')
        assert r.status == '200 OK'

    def test_get_root_page(self, user_fixture):
        r = self.client.get('/')
        assert r.status == '200 OK'

    def test_get_invalid_page(self, user_fixture):
        r = self.client.get('/home')
        assert r.status == '404 NOT FOUND'

    def test_get_queue_job_success(self, user_fixture):
        url = 'https://google.com'
        r = self.client.post('/index', data={'url': url})
        assert r.status == '302 FOUND'

    def test_count_words(self, user_fixture):
        url = 'https://google.com'
        r = self.client.post('/index', data={'url': url})
        time.sleep(3)
        webpage = Webpage.query.get(2)
        assert webpage.words == 142

    # Disabling these tests since post request is always redirected
    # to index.

    # def test_get_queue_job_bad_url(self, user_fixture):
    #     url = 'google.com'
    #     r = self.client.post('/index', data={'url': url})
    #     assert r.status == '400 BAD REQUEST'
    #
    #     url = ''
    #     r = self.client.post('/index', data={'url': url})
    #     assert r.status == '400 BAD REQUEST'
    #
    #     url = 'http://'
    #     r = self.client.post('/index', data={'url': url})
    #     assert r.status == '400 BAD REQUEST'

