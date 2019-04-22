def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Unsubscribe" in response.data
    assert b"Please enter your email address" in response.data
