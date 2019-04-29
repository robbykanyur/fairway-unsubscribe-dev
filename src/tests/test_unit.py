from app.models import User, Unsubscribe

def test_new_user():
    new_user = User(username='robb',email='robb@robb.com')
    new_user.set_password('the_correct_password')
    assert new_user.username == 'robb'
    assert new_user.email == 'robb@robb.com'
    assert new_user.check_password('the_incorrect_password') == False
    assert new_user.check_password('the_correct_password') == True

def test_new_unsubscribe():
    new_unsubscribe = Unsubscribe(email='bobb@bobb.com',address='1.1.1.1',sf_response='200',previously=True)
    assert new_unsubscribe.email == 'bobb@bobb.com'
    assert new_unsubscribe.address == '1.1.1.1'
    assert new_unsubscribe.sf_response == '200'
    assert new_unsubscribe.previously == True
