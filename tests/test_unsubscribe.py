def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Unsubscribe" in response.data
    assert b"Please enter your email address" in response.data

def test_admin_redirect(test_client):
    response = test_client.get('/admin')
    assert response.status_code == 302

def test_login_page(test_client):
    response = test_client.get('/login')
    assert response.status_code == 200 
    assert b"Sign In" in response.data
    assert b"Authenticate" in response.data

def test_new_unsubscribe(new_unsubscribe):
    assert new_unsubscribe.email == 'aaa@example.com'
    assert new_unsubscribe.timestamp == 'datetime.datetime(2019, 4, 14, 9, 44, 25, 391854)'
    assert new_unsubscribe.address == '1.1.1.1'
    assert new_unsubscribe.sf_response == '200'
    assert new_unsubscribe.previously == False


