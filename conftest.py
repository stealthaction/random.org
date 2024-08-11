from pages.main_page import MainPage
from playwright.sync_api import Page

import pytest


@pytest.fixture
def main_page(page: Page) -> MainPage:
    return MainPage(page)
