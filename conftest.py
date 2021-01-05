import pytest

from Pages.HomePage import HomePage


@pytest.fixture(scope="session")
def app(request):
    fixture = HomePage()
    request.addfinalizer(fixture.destroy)
    return fixture
