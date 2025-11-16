from app import app

def test_security_hidden_route():
    """
    SECURITY TEST: Attempts to access a route that shouldn't exist.
    Expects a 404 Not Found response.
    """
    test_client = app.test_client()
    response = test_client.get('/hidden_admin_page')
    assert response.status_code == 404