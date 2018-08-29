import pytest

from apps.config import conf
from apps.main import app_factory


@pytest.fixture
def app():
    return app_factory(conf)
