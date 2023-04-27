import unittest

from saucedemo_selenium_lib.config import TestConfig
from saucedemo_selenium_lib.saucedemo_utils import saucedemo_utils as sl
from tests.saucedemo.saucedemo_lib import (
    SaucedemoProductsLib,
    SaucedemoProductDetailLib,
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
    sort_type = [
        "Name (A to Z)",
        "Name (Z to A)",
        "Price (low to high)",
        "Price (high to low)",
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

    def test_sd_uc01_002_sort_items_in_the_products_catalogue_from_a_to_z(self):
        # use sort type from sort_type[0] for "Name (A to Z)"
        self.saucedemo_product_lib.sort_products(
            sort_type=self.sort_type[0],
        )

    def test_sd_uc01_003_sort_items_in_the_products_catalogue_from_z_to_a(self):
        # use sort type from sort_type[1] for "Name (Z to A)"
        self.saucedemo_product_lib.sort_products(
            sort_type=self.sort_type[1],
        )

    def test_sd_uc01_004_sort_items_in_the_products_catalogue_by_price_low_to_high(self):
        # use sort type from sort_type[2] for Price (low to high)"
        self.saucedemo_product_lib.sort_products(
            sort_type=self.sort_type[2],
        )

    def test_sd_uc01_005_sort_items_in_the_products_catalogue_by_price_high_to_low(self):
        # use sort type from sort_type[3] for Price (high to low)"
        self.saucedemo_product_lib.sort_products(
            sort_type=self.sort_type[3],
        )


class ViewProductDetails(BaseTestClass):
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
        self.saucedemo_product_detail_lib = SaucedemoProductDetailLib(saucedemo_utils)
        self.saucedemo_product_lib.log_in_saucedemo()

    def tearDown(self):
        self.saucedemo_product_lib.reset_app_state()
        self.saucedemo_product_lib.close_browser()

    def test_sd_uc02_001_click_the_product_image_to_get_detailed_info(self):
        product_name = self.product_names[0]
        self.saucedemo_product_lib.click_product_image(
            product_name=product_name,
        )
        self.saucedemo_product_detail_lib.verify_product_detail_is_open(
            product_name=product_name
        )

    def test_sd_uc02_002_click_the_product_name_to_get_detailed_info(self):
        product_name = self.product_names[0]
        self.saucedemo_product_lib.click_product_name(
            product_name=product_name,
        )
        self.saucedemo_product_detail_lib.verify_product_detail_is_open(
            product_name=product_name
        )
