import time
from app.app import app

def test_home_page_performance():
    """
    PERFORMANCE TEST: Measures how quickly the homepage responds.
    You might set an upper bound, e.g., <= 0.5 seconds.
    """
    test_client = app.test_client()
    start = time.time()
    response = test_client.get('/')
    end = time.time()
    elapsed = end - start
    assert elapsed < 0.5   # Page should respond quickly (adjust as needed)