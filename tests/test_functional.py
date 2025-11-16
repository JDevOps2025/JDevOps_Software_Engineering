import pytest
from app import app

def test_functional_main_page():
    """
    FUNCTIONAL TEST: Mimics a user visiting the home page. 
    Confirms key features or messages appear on the page.
    """
    test_client = app.test_client()
    response = test_client.get('/')
    assert response.status_code == 200
    page_content = response.data.decode('utf-8')
    assert "Your web server is running" in page_content  # Checks full message