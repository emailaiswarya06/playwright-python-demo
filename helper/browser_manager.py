from helper.configuration_manager import ConfigurationManager, ConfigurationManager1
from playwright.sync_api import Playwright, Browser, BrowserType
from helper.utils import read_config


class BrowserManager:
    @staticmethod
    def __get_browser_type(playwright: Playwright) -> BrowserType:
        #browser = ConfigurationManager.browser()
        browser =read_config('BROWSER', 'browser')
        print(f"browser inside browser manager {browser}")
        if browser == 'chromium':
            return playwright.chromium

        if browser == 'firefox':
            return playwright.firefox

        if browser == 'webkit':
            return playwright.webkit

    @staticmethod
    def initialize(playwright: Playwright) -> Browser:
        return BrowserManager.__get_browser_type(playwright).launch(headless=ConfigurationManager.headless(),
                                                                    channel=ConfigurationManager.browser_channel(),
                                                                    slow_mo=ConfigurationManager.slow_motion())

    @staticmethod
    def initialize1(playwright: Playwright) -> Browser:
        return BrowserManager.__get_browser_type(playwright).launch(headless=bool(ConfigurationManager1.headless()),
                                                                    channel=ConfigurationManager1.browser_channel(),
                                                                    slow_mo=ConfigurationManager1.slow_motion())

