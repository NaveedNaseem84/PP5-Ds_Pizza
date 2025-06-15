> [!NOTE]
> Return back to the [README.md](README.md) file.

# Testing

## Code Validation

### HTML

The code has been tested using the the official W3C validator [W3C HTML Validator.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fds-pizza-79dee8bcf8d6.herokuapp.com%2F). This has been used to validate all of my HTML files and the results are tabulated below:

| Directory  | File                                                                                                                                |  Live URL                                                                                                |           Screenshot                                                                            |    Notes |
| ---------- | --------------------------------------------------------------------------------------------------------                            | ---------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------------|--------- |
|home        | [index.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/home/templates/home/index.html)                               | [home](https://ds-pizza-79dee8bcf8d6.herokuapp.com/)                                                     | [Screenshot](readme-images/testing/validation/index-code-validation.png)                        | No Errors|
|menu        | [menu.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/menu/templates/menu/menu.html)                                 | [menu](https://ds-pizza-79dee8bcf8d6.herokuapp.com/menu/)                                                | [Screenshot](readme-images/testing/validation/menu-code-validation.png)                         | No Errors|
|about       | [about.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/about/templates/about/about.html)                             | [about](https://ds-pizza-79dee8bcf8d6.herokuapp.com/about/)                                              | [Screenshot](readme-images/testing/validation/about-code-validation.png)                        | No Errors|
|cart        | [cart.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/cart/templates/cart/cart.html)                                 | [cart](https://ds-pizza-79dee8bcf8d6.herokuapp.com/cart/)                                                | [Screenshot](readme-images/testing/validation/cart-code-validation.png)                         | No Errors|
|checkout    | [checkout.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/checkout/templates/checkout/checkout.html)                 | [checkout](https://ds-pizza-79dee8bcf8d6.herokuapp.com/checkout/)                                        | [Screenshot](readme-images/testing/validation/checkout-code-validation.png)                     | No Errors|
|checkout    | [myorders.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/checkout/templates/checkout/myorders.html)                 | [my orders](https://ds-pizza-79dee8bcf8d6.herokuapp.com/checkout/myorders/)                              | [Screenshot](readme-images/testing/validation/checkout-myorders-validation.png)                 | No Errors|
|checkout    | [success.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/checkout/templates/checkout/success.html)                   | [sucess](https://ds-pizza-79dee8bcf8d6.herokuapp.com/checkout/success/DS-6c59d8e7b8)                     | [Screenshot](readme-images/testing/validation/checkout-success-validation.png)                  | No Errors|
|management  | [management.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/management/templates/management/management.html)         | [management-order Dashboard](https://ds-pizza-79dee8bcf8d6.herokuapp.com/management/)                    | [Screenshot](readme-images/testing/validation/management-dashboard-validation.png)              | No Errors|
|management  | [update_status.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/management/templates/management/update_status.html)   | [management-update status](https://ds-pizza-79dee8bcf8d6.herokuapp.com/management/update_status/int:116) | [Screenshot](readme-images/testing/validation/update-order-status-validation.png)               | No Errors|
|templates   | [404.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/templates/404.html)                                             | N/A - testing using page source                                                                          | [Screenshot](readme-images/testing/validation/404-validation.png)                               | No Errors|
|templates   | [login.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/templates/account/login.html)                                 | [login](https://ds-pizza-79dee8bcf8d6.herokuapp.com/accounts/login/)                                     | [Screenshot](readme-images/testing/validation/login-validation.png)                             | No Errors|
|templates   | [register.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/templates/account/signup.html)                             | [register](https://ds-pizza-79dee8bcf8d6.herokuapp.com/accounts/signup/)                                 | [Screenshot](readme-images/testing/validation/register-validation.png)                          | No Errors|
|templates   | [logout.html](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/templates/account/logout.html)                               | [logout](https://ds-pizza-79dee8bcf8d6.herokuapp.com/accounts/logout/)                                   | [Screenshot](readme-images/testing/validation/logout-validation.png)                            | No Errors|


### CSS 

The code has been tested using the official W3C validator [W3C HTML Validator.](https://jigsaw.w3.org/css-validator)

| Directory  | File                                                                                         |  Live URL                                                                                                                                                                     |Screenshot                                                               |    Notes |
| ---------- | ---------------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------------|--------- |
|static      | [style.css](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/static/css/style.css)   | [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fds-pizza-79dee8bcf8d6.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=e)| [Screenshot](readme-images/testing/validation/css-validation.png)       | No Errors|



### JavaScript

The code has been validated using the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory         |File                                                                                                           |  Live URL   |  Screenshot                                                               |                                                        Notes |
| ------------------| --------------------------------------------------------------------------------------------------------------| ------------| --------------------------------------------------------------------------|------------------------------------------------------------- |
|static/about       | [mailchimp.js](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/static/js/about/mailchimp.js)         | N/A         | [Screenshot](readme-images/testing/validation/js-mailchimp-validation.png)| No Errors                                                    |
|static/cart        | [cart.js](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/static/js/cart/cart.js)                    | N/A         | [Screenshot](readme-images/testing/validation/js-cart-validation.png)     | No Errors                                                    |
|static/checkout    | [cart.js](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/static/js/checkout/stripe_elements.js)     | N/A         | [Screenshot](readme-images/testing/validation/js-stripe-validation.png)   | No Errors - one undefined variable (Stripe)*                 |
|static/management | [management.js](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/static/js/management/management.js)  | N/A         | [Screenshot](readme-images/testing/validation/js-stripe-validation.png)   | No Errors                                                     |

*Defined by the Stripe documentation as needed


### Python

The code has been validated using the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

*Ds_Pizza: Project*

| Directory   |File                                                                                            | URL                                                                                                                           |  Screenshot                                                                       |         Notes |
| ------------| -----------------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------------------------------------------| ----------------------------------------------------------------------------------|-------------- |               
|ds_pizza     | [settings.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/ds_pizza/settings.py)   | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/ds_pizza/settings.py)  | [Screenshot](readme-images/testing/validation/py-project-settings-validation.png) | No Errors     |
|ds_pizza     | [urls.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/ds_pizza/urls.py)           | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/ds_pizza/urls.py)      | [Screenshot](readme-images/testing/validation/py-project-urls-validation.png)     | No Errors     |


*About App:*

| Directory   |File                                                                                   | URL                                                                                                                     |  Screenshot                                                                  |         Notes |
| ------------| --------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------------------------------------| -----------------------------------------------------------------------------|-------------- |               
|about        | [admin.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/about/admin.py)   | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/about/admin.py)  | [Screenshot](readme-images/testing/validation/py-about-admin-validation.png) | No Errors     |
|about        | [models.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/about/models.py) | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/about/models.py) | [Screenshot](readme-images/testing/validation/py-about-models-validation.png)| No Errors     |
|about        | [test.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/about/tests.py)    | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/about/tests.py)  | [Screenshot](readme-images/testing/validation/py-about-tests-validation.png) | No Errors     |
|about        | [urls.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/about/urls.py)     | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/about/urls.py)   | [Screenshot](readme-images/testing/validation/py-about-urls-validation.png)  | No Errors     |
|about        | [views.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/about/views.py)   | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/about/views.py)  | [Screenshot](readme-images/testing/validation/py-about-views-validation.png) | No Errors     |


*Cart App:*

| Directory   |File                                                                                     | URL                                                                                                                     |  Screenshot                                                                    |         Notes |
| ------------| ----------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------------------------------------| -------------------------------------------------------------------------------|-------------- | 
|cart         | [admin.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/cart/admin.py)      | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/cart/admin.py)   | [Screenshot](readme-images/testing/validation/py-cart-admin-validation.png)    | No Errors     |
|cart         | [models.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/cart/models.py)    | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/cart/models.py)  | [Screenshot](readme-images/testing/validation/py-cart-models-validation.png)   | No Errors     |
|cart         | [contexts.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/cart/contexts.py)| [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/cart/contexts.py)| [Screenshot](readme-images/testing/validation/py-cart-contexts-validation.png) | No Errors     |
|cart         | [tests.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/cart/tests.py)      | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/cart/tests.py)   | [Screenshot](readme-images/testing/validation/py-cart-test-validation.png)     | No Errors     |
|cart         | [urls.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/cart/urls.py)        | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/cart/urls.py)    | [Screenshot](readme-images/testing/validation/py-cart-urls-validation.png)     | No Errors     |
|cart         | [utils.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/cart/utils.py)      | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/cart/utils.py)   | [Screenshot](readme-images/testing/validation/py-cart-utils-validation.png)    | No Errors     |
|cart         | [views.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/cart/views.py)      | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/cart/views.py)   | [Screenshot](readme-images/testing/validation/py-cart-views-validation.png)    | No Errors     |

*Checkout App:*

| Directory   |File                                                                                                   | URL                                                                                                                                  |  Screenshot                                                                               |         Notes |
| ------------| ------------------------------------------------------------------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------|-------------- |               
|checkout     | [admin.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/checkout/admin.py)                | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/checkout/admin.py)            | [Screenshot](readme-images/testing/validation/py-checkout-admin-validation.png)           | No Errors     |
|checkout     | [forms.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/checkout/forms.py)                | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/checkout/forms.py)            | [Screenshot](readme-images/testing/validation/py-checkout-forms-validation.png)           | No Errors     |
|checkout     | [models.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/checkout/models.py)              | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/checkout/forms.py)            | [Screenshot](readme-images/testing/validation/py-checkout-models-validation.png)          | No Errors     |
|checkout     | [tests.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/checkout/tests.py)                | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/checkout/tests.py)            | [Screenshot](readme-images/testing/validation/py-checkout-tests-validation.png)           | No Errors     |
|checkout     | [urls.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/checkout/urls.py)                  | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/checkout/urls.py)             | [Screenshot](readme-images/testing/validation/py-checkout-tests-validation.png)           | No Errors     |
|checkout     | [views.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/checkout/views.py)                | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/checkout/views.py)            | [Screenshot](readme-images/testing/validation/py-checkout-views-validation.png)           | No Errors     |
|checkout     | [webhook_handler.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/checkout/views.py)      | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/checkout/webhook_handler.py)  | [Screenshot](readme-images/testing/validation/py-checkout-webhook-handler-validation.png) | No Errors     |
|checkout     | [webhooks.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/checkout/webhooks.py)          | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/checkout/webhooks.py)         | [Screenshot](readme-images/testing/validation/py-checkout-webhook-validation.png)         | No Errors     |


*Home App:*

| Directory   |File                                                                                   | URL                                                                                                                     |  Screenshot                                                                  |         Notes |
| -----------| ---------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------------------------------------| -----------------------------------------------------------------------------|-------------- |               
|home        | [admin.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/home/admin.py)     | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/home/admin.py)   | [Screenshot](readme-images/testing/validation/py-home-admin-validation.png)  | No Errors     |
|home        | [models.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/home/models.py)   | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/home/models.py)  | [Screenshot](readme-images/testing/validation/py-home-models-validation.png) | No Errors     |
|home        | [tests.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/home/tests.py)     | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/home/tests.py)   | [Screenshot](readme-images/testing/validation/py-home-tests-validation.png)  | No Errors     |
|home        | [urls.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/home/urls.py)       | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/home/urls.py)    | [Screenshot](readme-images/testing/validation/py-home-urls-validation.png)   | No Errors     |
|home        | [views.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/home/views.py)     | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/home/views.py)   | [Screenshot](readme-images/testing/validation/py-home-views-validation.png)  | No Errors     |


*Management App:*

| Directory   |File                                                                                         | URL                                                                                                                           |  Screenshot                                                                        |         Notes |
| ------------| --------------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------------------------------------------| -----------------------------------------------------------------------------------|-------------- |               
|management   | [admin.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/management/admin.py)    | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/management/admin.py)   | [Screenshot](readme-images/testing/validation/py-management-admin-validation.png)  | No Errors     |
|management   | [forms.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/management/forms.py)    | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/management/forms.py)   | [Screenshot](readme-images/testing/validation/py-management-forms-validation.png)  | No Errors     |
|management   | [models.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/management/models.py)  | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/management/models.py)  | [Screenshot](readme-images/testing/validation/py-management-models-validation.png) | No Errors     |
|management   | [tests.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/management/tests.py)    | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/management/tests.py)   | [Screenshot](readme-images/testing/validation/py-management-tests-validation.png)  | No Errors     |
|management   | [urls.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/management/urls.py)      | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/management/urls.py)    | [Screenshot](readme-images/testing/validation/py-management-urls-validation.png)   | No Errors     |
|management   | [views.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/management/views.py)    | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/management/views.py)   | [Screenshot](readme-images/testing/validation/py-management-views-validation.png)  | No Errors     |

*Menu App:*

| Directory   |File                                                                                         | URL                                                                                                                       |  Screenshot                                                                        |         Notes |
| ------------| --------------------------------------------------------------------------------------------| --------------------------------------------------------------------------------------------------------------------------| -----------------------------------------------------------------------------------|-------------- |               
|menu         | [admin.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/menu/admin.py)          | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/menu/admin.py)     | [Screenshot](readme-images/testing/validation/py-menu-admin-validation.png)        | No Errors     |
|menu         | [models.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/menu/models.py)        | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/menu/models.py)    | [Screenshot](readme-images/testing/validation/py-menu-models-models-validation.png)| No Errors     |
|menu         | [tests.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/menu/tests.py)          | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/menu/tests.py)     | [Screenshot](readme-images/testing/validation/py-menu-tests-validation.png)        | No Errors     |
|menu         | [urls.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/menu/urls.py)            | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/menu/urls.py)      | [Screenshot](readme-images/testing/validation/py-menu-urls-validation.png)         | No Errors     |
|menu         | [views.py](https://github.com/NaveedNaseem84/PP5-Ds_Pizza/blob/main/menu/views.py)          | [link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/NaveedNaseem84/PP5-Ds_Pizza/main/menu/views.py)     | [Screenshot](readme-images/testing/validation/py-menu-views-validation.png)        | No Errors     |



## Fixed Bugs

### Issue 1 (ID: f5c1c2e)

The current "max" value for the quantity is set to 10. Using inspect on this quantity field allows for the max quantity to be set to any therefore bypassing the default max value.

- Reproduced by:
  - View a product
  - Right click on quantity field and manually change the max value. eg. 1000
  - Add item to bag
  - 1000 selected item added to bag 

### Fix: (ID:a4116e4)

 This was fixed by implementing the following logic:
    1. If the item is already in the cart, a python check allows a maximum increase to 10.
    2. If the quantity is being added via the add to bag, a python check has been introduced to ensure the quantity is not over 10.
 In both cases a notification is given letting the user know. 

 ### Issue 2 (ID: 914df78)

 If a pizza (as an example) is already in the cart, and another pizza is added, the original pizza is replaced with the new one. The same issue occurred with the other items,

The item total/grand total were also affected as as result of this. Quantity for said items not affected.

- Reproduced by:
  - View a product
  - Add item to basket.
  - Item seen in basket.
  - Add another item in same category to bag
  - 1000 selected item added to bag
  - item over written

### Fix: (ID: 914df78)

On re-visiting the affected code, it was discovered that a section of was indented incorrectly and therefore not sitting correctly within the loop. Indenting this into the correct location and a retest found the issue to be resolved.


### Issue 3(ID: N/a)
**Please note** This was a general discovery whilst coding and documented.

If a new pizza is added to the database, and the gf/veg option are not exclusively set, the filter will not work correctly pick up this new addition.

- Reproduced by:
  - Login in as admin
  - Add new pizza
  - Fill in form - leave out is_veg and/or is_gf (i.e. not set to no or yes)
  - Save the form
  - Apply the filter to find veg or gf options.

### Fix: (ID:a65a57c)
This was fixed by updating the pizza modal to make the is_veg and is_gf feels mandatory. Once adjusted and migrated, a restest found the filter working as it should be.


