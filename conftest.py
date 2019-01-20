import pytest
from fixture.application import Application
from fixture.contact_fixture import Сontact_fixture

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



@pytest.fixture
def con_fix(request):
    fixture = Сontact_fixture()
    request.addfinalizer(fixture.destroy)
    return fixture

