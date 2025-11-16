import pytest
from app import app

def test_home_route_integration():
    """
    INTEGRATION TEST: Verifies the Flask app and static file serving work together.
    Uses Flask's test client to make a request to '/' and checks the response.
    """
    test_client = app.test_client()
    response = test_client.get('/')
    assert response.status_code == 200   # Confirms server is running
    assert b"AI & MACHINE LEARNING" in response.data     # Looks for content in the returned HTML