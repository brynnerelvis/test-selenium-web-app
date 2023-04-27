"""
Locators for saucedemo
"""

from selenium.webdriver.common.by import By


class SauceDemoProductsPageLocators:
    PRODUCTS_TITLE = (By. XPATH, "//span[contains(@class, 'title') and contains(., 'Products')]")


class SauceDemoProductsDetailLocators:
    BACK_TO_PRODUCTS_BUTTON = (By.ID, "back-to-products")
    DETAIL_NAME = (By. CLASS_NAME, "inventory_details_name")
    DETAIL_DESCRIPTION = (By.CLASS_NAME, "inventory_details_desc")
    DETAIL_PRICE = (By.CLASS_NAME, "inventory_details_price")