"""
Locators for saucedemo
"""

from selenium.webdriver.common.by import By


class SauceDemoProductsPageLocators:
    PRODUCTS_TITLE = (By. XPATH, "//span[contains(@class, 'title') and contains(., 'Products')]")
