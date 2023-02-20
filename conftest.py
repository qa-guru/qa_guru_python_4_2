import pytest


@pytest.fixture()
def teardown():
    yield
    print("do something")


@pytest.fixture(scope="session")
def browser():
    print("Открываем браузер")
    yield "Chrome"
    print("Закрываем браузер")
