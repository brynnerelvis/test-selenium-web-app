""""
For adding tests fixtures
"""

import os

import pytest

from saucedemo_selenium_lib.config import TestConfig
from saucedemo_selenium_lib.data_models import WebBrowsers


def pytest_addoption(parser):
    parser.addoption("--host_index", action="store", default="0")
    parser.addoption("--headless", action="store", default="1")
    parser.addoption("--proxy", action="store", default=None)
    parser.addoption("--runner", action="store", default="app")
    parser.addoption("--url", action="store", default="https://www.saucedemo.com/")
    parser.addoption("--username", action="store", default="standard_user")
    parser.addoption("--password", action="store", default="secret_sauce")
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Web browser that selenium tests will be run on. Available options include 'chrome' and 'firefox'. "
        "Default is chrome",
    )


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """


@pytest.fixture(scope="session")
def host_index(request):
    index_value = request.config.option.host_index
    return index_value


@pytest.fixture(scope="session", autouse=True)
def create_test_config(request):
    runner = request.config.option.runner
    browser_arg = request.config.option.browser
    if browser_arg == "firefox":
        browser = WebBrowsers.FIREFOX
    elif browser_arg == "chrome":
        browser = WebBrowsers.CHROME
    else:
        raise AssertionError(f"--browser argument: {browser_arg}")
    if runner == "app":
        url = request.config.option.url
        username = request.config.option.username
        password = request.config.option.password
        config_test = TestConfig(
            host_url=url, username=username, password=password, browser=browser
        )
    else:
        index_value = request.config.option.host_index

        if index_value is not None:

            index_value = int(index_value)
            config_test = TestConfig(host_index=index_value, browser=browser)
            if not os.path.exists(config_test.config_file_path):
                # check that the config path exists
                raise AssertionError(
                    f"config.yml file containing Saucedemo Instance configs not found. Please add it in the given path: {config_test.config_file_path}.",
                )
        else:
            raise AssertionError("the host index Value not defined")
    return config_test


@pytest.fixture(scope="class", autouse=True)
def config_class(request, create_test_config):
    """Get commandline options and Change test classes attributes during runtime.
    Set autouse to True so that pytest automically decorate the Test case classes"""
    headless = request.config.option.headless
    if headless is not None:
        if int(headless) == 1:
            request.cls.headless = True
        else:
            request.cls.headless = False
    proxy = request.config.option.proxy
    request.cls.proxy = proxy
    request.cls.config = create_test_config


def pytest_html_report_title(report):
    """Change HTML Report title"""

    report.title = f"Selenium Tests for Report"
