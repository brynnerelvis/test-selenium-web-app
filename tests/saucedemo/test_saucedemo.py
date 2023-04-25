import unittest

from saucedemo_selenium_lib.config import TestConfig
from saucedemo_selenium_lib.saucedemo_utils import saucedemo_utils as sl
from tests.saucedemo.saucedemo_lib import (
    SaucedemoProductsLib,
)


class BaseTestClass(unittest.TestCase):
    config = TestConfig(host_index=0)
    headless = True
    product_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() Tshirt",
    ]

class BrowsingAndFilteringCatalogue(BaseTestClass):
    def setUp(self):
        saucedemo_utils = sl.SaucedemoUtils(
            host_url=self.config.host_url,
            username=self.config.username,
            password=self.config.password,
            headless=self.headless,
            browser=self.config.browser,
            grid=self.config.grid,
        )
        self.saucedemo_product_lib = SaucedemoProductsLib(saucedemo_utils)
        self.saucedemo_product_lib.log_in_saucedemo()

    def tearDown(self):
        self.saucedemo_product_lib.reset_app_state()
        self.saucedemo_product_lib.close_browser()

    def test_sd_uc01_001_view_the_products_catalogue(self):
        self.saucedemo_product_lib.view_products_catalogue(
            product_names=self.product_names,
        )
