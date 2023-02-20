import random

import pytest


@pytest.fixture
def get_admin(browser, teardown):
    return random.randint(0, 100)


def test_simple(get_admin, browser):
    # assert get_admin == 5, "Айдишник администратора ожидался 5"
    # assert browser == "Chrome"
    print(browser)
    assert 1 == 1, "Единица не должна быть равна двойке"


def test_another(browser, get_admin):
    print(browser)
    # assert get_admin == 5, "Айдишник администратора ожидался 5"
    assert 1 == 1, "Единица не должна быть равна двойке"
