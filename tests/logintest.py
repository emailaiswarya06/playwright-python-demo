import logging

import pytest
from playwright.sync_api import Playwright, Page

from helper.browser_manager import BrowserManager
from pages.login_page import LoginPage


def test_correct_username_and_correct_password(playwright_browser_context):
    logging.info("before login page")
    page = playwright_browser_context
    login_page = LoginPage(page)
    #login_page.dummy()
    login_page.enter_username().enter_password().click_login()
