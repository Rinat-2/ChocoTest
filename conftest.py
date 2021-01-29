import pytest

from Pages.HomePage import HomePage
from Pages.TicketsPage import TicketsPage


@pytest.fixture(scope="session")
def app(request):
    fixture = HomePage() or TicketsPage()
    request.addfinalizer(fixture.destroy)
    return fixture

# @pytest.fixture(scope="session")
# def app(request):
#    driver = webdriver.Chrome()
#    driver.implicitly_wait(60)
#    request.addfinalizer(driver.quit)
#    return driver

# @pytest.fixture(scope="session")
# def browser():
#    driver = webdriver.Chrome()
#    yield driver
#    driver.quit()
