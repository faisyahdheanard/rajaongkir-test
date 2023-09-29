import pytest

@pytest.fixture(scope='function', autouse=True)
def hook(request):
    # print("\nbefore test")
    yield
    # print("after test")

@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # print("\nbefore suite")
    yield
    # print("after suite")
