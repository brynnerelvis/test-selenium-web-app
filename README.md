# test-selenium-web-app

This is a dedicated selenium test for the website https://www.saucedemo.com/. 

<style>
p{color:Red !important;}
</style>

# Tests Coverage
### Atonomy of the Test Case ID: 

Example: _sd_uc01_001_

_sd_: The first letter represents short for the application that is in test. (Here we use _sd_ because the application is called Sauce Demo).

_uc01_: This is to indicate which usecase the test belongs to. (Here we use _uc01_ which represents Use Case 1).

_001_: This is to indicate the number of the test case. (Here we use _001_ to indicate that this is the first test case for the usecase).



## Use Case 1: Browsing and Filtering Catalog

Test Case ID | Test Case Name | Test Case Category | Test Data | Preconditions | Test Steps | Expected Outcome | Selenium Coverage | Manual Coverage |
--- | --- | --- | --- |--- |--- |--- |--- |--- |
sd_uc01_001 |View The Products Catalogue| Critical | - | <ul><li>Standard User Credentials  |<br> 1. Log in with the standard user credentials <br>2. View the products catalogue page | <ul><li>The products catalogue page is present |   |   |
sd_uc01_002 |Filter items in the products catalogue from A to Z| Normal | - | <ul><li>Standard User Log In is succesful |<br> 1. Log in with the standard user credentials <br>2. View the products catalogue page <br>3. Click the filter drop down button <br>4. Select the "Name (A to Z)" fromt the list | <ul><li>The products catalogue page was updated with products arranged by alphabetical order <ul><li>Filter drop down button updated with "Name (A to Z)"|   |   |
sd_uc01_003 |Filter items in the products catalogue from Z to A| Normal | - | <ul><li>Standard User Log In is succesful |<br> 1. Log in with the standard user credentials <br>2. View the products catalogue page <br>3. Click the filter drop down button <br>4. Select the "Name (Z to A)" fromt the list | <ul><li>The products catalogue page was updated with products arranged by reversed alphabetical order <ul><li>Filter drop down button updated with "Name (Z to A)"|   |   |
sd_uc01_004 |Filter items in the products catalogue by price low to high| Normal | - | <ul><li>Standard User Log In is succesful |<br> 1. Log in with the standard user credentials <br>2. View the products catalogue page <br>3. Click the filter drop down button <br>4. Select the "Price (Low to High)" from the list | <ul><li>The products catalogue page was updated with products arranged by price, low to high <ul><li>Filter drop down button updated with "Price (Low to High)"|   |   |
sd_uc01_005 |Filter items in the products catalogue by price high to low| Normal | - | <ul><li>Standard User Log In is succesful |<br> 1. Log in with the standard user credentials <br>2. View the products catalogue page <br>3. Click the filter drop down button <br>4. Select the "Price (High to Low)" from the list | <ul><li>The products catalogue page was updated with products arranged by price, high to low <ul><li>Filter drop down button updated with "Price (High to Low)"|   |   |

  
## Use Case 2: View Product Details

Test Case ID | Test Case Name | Test Case Category | Test Data | Preconditions | Test Steps | Expected Outcome | Selenium Coverage | Manual Coverage |
--- | --- | --- | --- |--- |--- |--- |--- |--- |
sd_uc02_001 |Click the product image to get detailed info| Critical | - | <ul><li>Standard User Credentials  |<br> 1. Log in with the standard user credentials <br>2. At products page, click on a product image | <ul><li>The product's detail page is open |   |   |
sd_uc02_002 |Click the product name to get detailed info| Critical | - | <ul><li>Standard User Credentials  |<br> 1. Log in with the standard user credentials <br>2. At products page, click on a product name | <ul><li>The product's detail page is open |   |   |

  
## Use Case 3: Managing Products in Cart

Test Case ID | Test Case Name | Test Case Category | Test Data | Preconditions | Test Steps | Expected Outcome | Selenium Coverage | Manual Coverage |
--- | --- | --- | --- |--- |--- |--- |--- |--- |
sd_uc03_001 | View cart icon notification after adding one product to the cart| Critical | - | <ul><li>Standard User Credentials  |<br> 1. Log in with the standard user credentials <br>2. At products page, add a product to cart <br>3. Check the cart icon notification | <ul><li>The cart icon notification is "1" |   |   |
sd_uc03_002 | View cart after adding one product to the cart| Critical | - | <ul><li>Standard User Credentials  |<br> 1. Log in with the standard user credentials <br>2. At products page, add a product to cart <br>3. Click the cart icon | <ul><li>The added product is present in the cart |   |   |
sd_uc03_003 | View cart icon notification after adding all products to the cart| Critical | - | <ul><li>Standard User Credentials  |<br> 1. Log in with the standard user credentials <br>2. At products page, add all products to cart <br>3.  Check the cart icon notification | <ul><li>The cart icon notification is "6" |   |   |
sd_uc03_004 | View cart after adding all products to the cart| Critical | - | <ul><li>Standard User Credentials  |<br> 1. Log in with the standard user credentials <br>2. At products page, add all products to cart <br>3. Click the cart icon | <ul><li>The products are present in the cart |   |   |
sd_uc03_005 | View cart icon notification after removing one product after selecting in products page| Critical | - | <ul><li>Standard User Credentials  |<br> 1. Log in with the standard user credentials <br>2. At products page, add one product to cart <br>3. Check the cart icon notification is "1" <br>4. Click the remove button at the selected product <br>5. From the cart, remove 1 product <br>6. Check the cart is updated with 1 product left <br>7. Return to the products page <br>8. Check the cart icon notification | <ul><li>There is not cart icon notification |   |   |
  
## Use Case 4: Checkout and Purchasing

Test Case ID | Test Case Name | Test Case Category | Test Data | Preconditions | Test Steps | Expected Outcome | Selenium Coverage | Manual Coverage |
--- | --- | --- | --- |--- |--- |--- |--- |--- |
sd_uc04_001 | Purchase all products in the cart | Critical | - | <ul><li>Standard User Credentials  |<br> 1. Log in with the standard user credentials <br>2. At the products page, add 2 products to the cart <br>3. Click the cart icon <br>4. At the cart page, click checkout button <br>5. At the Your Informations page, fill in the information details (First Name, Last Name, Zip/Postal Code) <br>6. Click the Continue button <br>7. At the overview page, click the Finish Button | <ul><li>Navigated to the complete page <ul><li>The complete order message appears <ul><li>The Back Home button is visible |   |   |
