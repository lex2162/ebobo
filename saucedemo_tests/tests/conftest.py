import pytest
from ..pages.chrome import ChromeDriver
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture
def browser():
    driver = ChromeDriver()
    yield driver
    driver.driver.quit()
