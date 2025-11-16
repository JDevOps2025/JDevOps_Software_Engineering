import sys
import os
import pytest
from app.app import app


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_security_hidden_route():
    """
    SECURITY TEST: Attempts to access a route that shouldn't exist.
    Expects a 404 Not Found response.
    """
    test_client = app.test_client()
    response = test_client.get('/hidden_admin_page')
    assert response.status_code == 404