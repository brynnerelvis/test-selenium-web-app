"""
Library classes of methods used for sauce demo tests.
"""

from saucedemo_selenium_lib.saucedemo_core.saucedemo_page import BaseSaucedemoPage
from src.locators import SauceDemoProductsPageLocators


class SaucedemoProductsLib(BaseSaucedemoPage):
    """Class for lirbary of methods used in the Products page of Saucedemo webapp"""
    def view_products_catalogue(self, product_names: list):
        """
        Checks the presence of the products title element
        and check products in the product list.

        Args:
            product_names: list

        Return:
            None

        """
        self.__check_presence_of_product_title()
        for product_name in product_names:
            self.verify_if_product_is_present(
                product_name=product_name,
            )

    def __check_presence_of_product_title(self):
        """
        Assert the products title element on the page.

        """
        assert self.saucedemo_utils.is_element_available(
            locator=SauceDemoProductsPageLocators.PRODUCTS_TITLE,
        )
