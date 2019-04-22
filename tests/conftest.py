import os
import sys
import pytest
from app import create_app
from app.models import User, Unsubscribe

collect_ignore = ['node_modules']

@pytest.fixture(scope='module')
def new_user():
    u = User(username="bobb",email="bobb@example.com")
    u.set_password('bobbbobb')
    return u

@pytest.fixture(scope='module')
def new_unsubscribe():
    unsb = Unsubscribe(email='aaa@example.com',
                       timestamp='datetime.datetime(2019, 4, 14, 9, 44, 25, 391854)',
                       address='1.1.1.1',
                       sf_response='200',
                       previously=False)
    return unsb

@pytest.fixture(scope='module')
def test_client():
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    DB_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app_test.db')

    flask_app = create_app()
    flask_app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI=DB_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_ENABLED=False
    )

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    db.create_all()

    u1 = Unsubscribe(email='aaa@example.com',
                     timestamp='datetime.datetime(2019, 4, 14, 9, 44, 25, 391854)',
                     address='1.1.1.1',
                     sf_response='200',
                     previously=True)

    u2 = Unsubscribe(email='bbb@example.com',
                     timestamp='datetime.datetime(2019, 4, 14, 9, 44, 25, 391854)',
                     address='2.2.2.2',
                     sf_response='500',
                     previously=False)

    db.session.add(unsubscribe1)
    db.session.add(unsubscribe2)

    db.session.commit()

    yield db

    db.drop_all()
