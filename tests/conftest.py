import pytest
from app.models import User
 
 
@pytest.fixture(scope='module')
def new_user():
    u = User(username='esther')
    u.set_password('password1')
    return u
    