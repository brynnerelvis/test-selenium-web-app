"""
Library classes of methods used for sauce demo tests.
"""
from selenium.webdriver.common.by import By

from saucedemo_selenium_lib.saucedemo_core.saucedemo_page import BaseSaucedemoPage
from src.locators import SauceDemoProductsPageLocators, SauceDemoProductsDetailLocators


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
        assert self.__check_presence_of_product_title()
        for product_name in product_names:
            self.verify_if_product_is_present(
                product_name=product_name,
            )

    def __check_presence_of_product_title(self):
        """
        Checks the products title element on the page
        and returns True if found, else returns False.

        Return:
            Boolean

        """
        return self.saucedemo_utils.is_element_available(
            locator=SauceDemoProductsPageLocators.PRODUCTS_TITLE,
        )

    def __is_price_list_sorted(self, price_list, sort_type):
        """
        Checks the product price list sorted according to
        the sort type, and returns a boolean value:
            True if sorted
            False if not sorted

        Args:
            price_list: list
            sort_type: str

        Return:
            boolean

        """
        # Convert price strings to float values
        float_prices = [float(price[1:]) for price in price_list]

        if sort_type == "Price (low to high)":
            return all(price1 <= price2 for price1, price2
                       in zip(float_prices, float_prices[1:]))
        elif sort_type == "Price (high to low)":
            return all(price1 >= price2 for price1, price2
                       in zip(float_prices, float_prices[1:]))
        else:
            raise ValueError("Invalid sort type")

    def __is_product_names_list_sorted(self, product_names_list: list, sort_type: str):
        """
        Checks the product names list sorted according to
        the sort type, and returns a boolean value:
            True if sorted
            False if not sorted

        Args:
            product_names_list: list
            sort_type: str

        Return:
            boolean

        """
        if sort_type == "Name (A to Z)":
            return all(product1 <= product2 for product1, product2
                       in zip(product_names_list, product_names_list[1:]))
        elif sort_type == "Name (Z to A)":
            return all(product1 >= product2 for product1, product2
                       in zip(product_names_list, product_names_list[1:]))
        else:
            raise ValueError("Invalid sort order")

    def sort_products(self, sort_type: str):
        """
        Sorts the products by selecting a sort type
        from the sort drop down list and assert if the
        products are sorted.

        Args:
            sort_type: str

        Return:
            None

        """
        # sort the product list based on the sort type
        self.sort_product_list(sort_type=sort_type)

        # assert if the product list was sorted
        if sort_type == "Name (A to Z)" or sort_type == "Name (Z to A)":
            product_names_list = self.saucedemo_utils.get_product_names()
            assert self.__is_product_names_list_sorted(
                sort_type=sort_type,
                product_names_list=product_names_list,
            )
        elif sort_type == "Price (low to high)" or sort_type == "Price (high to low)":
            price_list = self.saucedemo_utils.get_product_prices()
            assert self.__is_price_list_sorted(
                sort_type=sort_type,
                price_list=price_list
            )
        else:
            raise ValueError("Invalid sort order")

    def click_product_image(self, product_name):
        """
        Clicks on the product image based on the product
        name.

        Args:
            product_name: str

        Return:
            None

        """
        self.select_product_by_image(product_name)

    def click_product_name(self, product_name):
        """
        Clicks on the product name.

        Args:
            product_name: str

        Return:
            None

        """
        self.select_product_by_name(product_name)


class SaucedemoProductDetailLib(BaseSaucedemoPage):
    """Class for the product detail page of Saucedemo webapp"""

    def verify_product_detail_is_open(self, product_name: str):
        """
        Assert the name of the product and the back to products
        button in the product detail page.

        Args:
             product_name: str

        Return:
            None

        """
        assert self.__check_presence_of_back_to_products_button()
        assert self.__check_presence_of_detail_product_name(
            product_name=product_name,
        )


    def __check_presence_of_detail_product_name(self, product_name: str):
        """
        Checks the product name on the detail page and returns
        True if found, else returns False.

        Args:
            product_name: str

        Return:
            Boolean

        """
        detail_product_name_locator = (
            By.XPATH,
            f"//div[contains(@class, 'inventory_details_name') "
            f"and contains(., '{product_name}')]"
        )
        return self.saucedemo_utils.is_element_available(
            locator=detail_product_name_locator,
        )

    def __check_presence_of_back_to_products_button(self):
        """
        Checks the back to products button element on the
        page and returns True if found, else returns False.

        Return:
            Boolean

        """
        return self.saucedemo_utils.is_element_available(
            locator=SauceDemoProductsDetailLocators.BACK_TO_PRODUCTS_BUTTON,
        )