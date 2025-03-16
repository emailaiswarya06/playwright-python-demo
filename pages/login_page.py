import logging

from playwright.sync_api import Page

from helper.configuration_manager import ConfigurationManager


class LoginPage:


    def __init__(self,page:Page):
        self.current_page = page

    def enter_username(self):
        self.current_page.fill('id=user-name', 'standard_user')
        return self

    def enter_password(self):
        self.current_page.fill('id=password', 'secret_sauce')
        return self

    def click_login(self):
        self.current_page.click('id=login-button')

    def dummy(self):
        logging.info("Dummy inside login test")
        pass