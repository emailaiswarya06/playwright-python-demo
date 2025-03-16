import logging
from multiprocessing import get_logger

import pytest
from playwright.sync_api import Playwright, sync_playwright

from helper.browser_manager import BrowserManager
from helper.utils import read_config


@pytest.fixture()
def playwright_browser(playwright: Playwright):
    #return BrowserManager.initialize(playwright)
    return BrowserManager.initialize1(playwright)

@pytest.fixture()
def playwright_browser_context(playwright_browser):
    logging.info("Creating New Browser Context")
    print("Creating New Browser Context")

    context = playwright_browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto(read_config('DEV', 'base_url'))

    yield page  # Provide the page to the test

    logging.info("Closing Browser Context")
    context.close()
    page.close()


def sanity(func):
    """Custom decorator to apply multiple pytest markers."""
    func = pytest.mark.sanity(func)
    func = pytest.mark.xdist_group(name="group1")(func)
    return func

def regression(func):
    """Custom decorator to apply multiple pytest markers."""
    func = pytest.mark.regression(func)
    func = pytest.mark.xdist_group(name="group2")(func)
    return func

def smoke(func):
    """Custom decorator to apply multiple pytest markers."""
    func = pytest.mark.smoke(func)
    func = pytest.mark.xdist_group(name="group3")(func)
    return func

#Not a working solution currently
def smokeandregression(func):
    """Custom decorator to apply multiple pytest markers."""
    func = pytest.mark.regression(func)
    func = pytest.mark.xdist_group(name="group2")(func)
    func = pytest.mark.smoke(func)
    func = pytest.mark.xdist_group(name="group3")(func)
    return func


# Configure logging for parallel execution
def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(process)d] [%(levelname)s] - %(message)s",
    )

    # Ensure logs from worker processes are captured
    logger = get_logger()
    logger.setLevel(logging.INFO)

configure_logging()  # Apply logging before tests start
