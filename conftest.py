from app import create_app
from app.models import User
import pytest

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture(scope='module')
def new_user():
    user = User(username='bobb', email='bobb@bobb.com')
    user.set_password('bobb')
    return user
