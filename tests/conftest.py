import pytest
from app import create_app
from app.utilities import test_rebuild

app = create_app(config_module='app.configs.test_config')


@pytest.fixture(scope='session')
def setup():
    # Get the app context and push it
    ctx = app.app_context()
    ctx.push()
    test_rebuild()
    yield app
    ctx.pop()


@pytest.fixture(scope='class')
def user_fixture(request):
    # Setup code
    client = app.test_client()
    request.cls.client = client

