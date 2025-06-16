> [!NOTE]
> Return back to the [README.md](README.md) file.

# Testing

Add in summary and links to what is included

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

> [!NOTE]
> Return back to the [README.md](README.md) file.

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

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Lighthouse Scores

The site has been tested using the Lighthouse Audit tool to check for any major issues. It was tested for both mobile and desktop views, and the results are tabulated below:


| Page         | Mobile                                                                       | Desktop                                                                      |
| -------------| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
|Register      |[Screenshot](readme-images/testing/lighthouse/lighthouse-register-mobile.png) | [Screenshot](readme-images/testing/lighthouse/lighthouse-register-desktop.png)
|Login         |[Screenshot](readme-images/testing/lighthouse/lighthouse-login-mobile.png)    | [Screenshot](readme-images/testing/lighthouse/lighthouse-login-desktop.png)
|logout        |[Screenshot](readme-images/testing/lighthouse/lighthouse-logout-mobile.png)   | [Screenshot](readme-images/testing/lighthouse/lighthouse-logout-desktop.png)
|Home          |[Screenshot](readme-images/testing/lighthouse/lighthouse-home-mobile.png)     | [Screenshot](readme-images/testing/lighthouse/lighthouse-home-desktop.png)
|Menu          |[Screenshot](readme-images/testing/lighthouse/lighthouse-menu-mobile.png)     | [Screenshot](readme-images/testing/lighthouse/lighthouse-menu-desktop.png)
|About us      |[Screenshot](readme-images/testing/lighthouse/lighthouse-about-mobile.png)    | [Screenshot](readme-images/testing/lighthouse/lighthouse-about-desktop.png)
|Cart          |[Screenshot](readme-images/testing/lighthouse/lighthouse-cart-mobile.png)     | [Screenshot](readme-images/testing/lighthouse/lighthouse-cart-desktop.png)
|Checkout      |[Screenshot](readme-images/testing/lighthouse/lighthouse-checkout-mobile.png) | [Screenshot](readme-images/testing/lighthouse/lighthouse-checkout-desktop.png)
|Success       |[Screenshot](readme-images/testing/lighthouse/lighthouse-success-mobile.png)  | [Screenshot](readme-images/testing/lighthouse/lighthouse-success-desktop.png)
|My Orders     |[Screenshot](readme-images/testing/lighthouse/lighthouse-myorders-mobile.png) | [Screenshot](readme-images/testing/lighthouse/lighthouse-myorders-desktop.png)
|Add Item      |[Screenshot](readme-images/testing/lighthouse/lighthouse-additem-mobile.png)  | [Screenshot](readme-images/testing/lighthouse/lighthouse-additem-desktop.png)
|Edit Item     |[Screenshot](readme-images/testing/lighthouse/lighthouse-edititem-mobile.png) | [Screenshot](readme-images/testing/lighthouse/lighthouse-edititem-desktop.png)
|404           |[Screenshot](readme-images/testing/lighthouse/lighthouse-404-mobile.png)      | [Screenshot](readme-images/testing/lighthouse/lighthouse-404-desktop.png)


During the course of the lighthouse testing it was found that there were certain warnings that fell beyound the scope of my control, and that results on mobile tended to be lower across the board.

## Browser Testing

The site has been deployed and tested on multiple desktop browser to check for any compatibility issues, and the results are documented below:

| Page                    | Edge                                                                       | Chrome                                                                         | Firefox                                                               | Outcome   |
| ------------------------| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------|-----------------------------------------------------------------------|-----------|
|Register                 | [Screenshot](readme-images/testing/browser/edge-register.png)              |  [Screenshot](readme-images/testing/browser/chrome-register.png)               |[Screenshot](readme-images/testing/browser/moz-register.png)           | No issues |
|Login                    | [Screenshot](readme-images/testing/browser/edge-login.png)                 |  [Screenshot](readme-images/testing/browser/chrome-login.png)                  |[Screenshot](readme-images/testing/browser/moz-login.png)              | No issues |
|logout                   | [Screenshot](readme-images/testing/browser/edge-logout.png)                |  [Screenshot](readme-images/testing/browser/chrome-logout.png)                 |[Screenshot](readme-images/testing/browser/moz-logout.png)             | No issues |
|Home                     | [Screenshot](readme-images/testing/browser/edge-home.png)                  |  [Screenshot](readme-images/testing/browser/chrome-home.png)                   |[Screenshot](readme-images/testing/browser/moz-home.png)               | No issues |
|Menu                     | [Screenshot](readme-images/testing/browser/edge-menu.png)                  |  [Screenshot](readme-images/testing/browser/chrome-menu.png)                   |[Screenshot](readme-images/testing/browser/moz-menu.png)               | No issues |
|Menu-item details        | [Screenshot](readme-images/testing/browser/menu-product-details.png)       |  [Screenshot](readme-images/testing/browser/chrome-menu-details.png)           |[Screenshot](readme-images/testing/browser/moz-menu-details.png)       | No issues |
|Menu-Add to cart         | [Screenshot](readme-images/testing/browser/edge-add-cart.png)              |  [Screenshot](readme-images/testing/browser/chrome-add-to-cart.png)            |[Screenshot](readme-images/testing/browser/moz-add-to-cart.png)        | No issues |
|Menu-Increase quantity   | [Screenshot](readme-images/testing/browser/edge-increase-quantity.png)     |  [Screenshot](readme-images/testing/browser/chrome-increase-quantity.png)      |[Screenshot](readme-images/testing/browser/moz-increase-quantity.png)  | No issues |
|Menu-Decrease quantity   | [Screenshot](readme-images/testing/browser/edge-decrease-qty.png)          |  [Screenshot](readme-images/testing/browser/chrome-decrease-quantity.png)      |[Screenshot](readme-images/testing/browser/moz-decrease-quantity.png)  | No issues |
|Menu-max quantity        | [Screenshot](readme-images/testing/browser/edge-max-quantity.png)          |  [Screenshot](readme-images/testing/browser/chrome-max-quantity.png)           |[Screenshot](readme-images/testing/browser/moz-max-quantity.png)       | No issues |
|Menu-remove all          | [Screenshot](readme-images/testing/browser/edge-remove-all.png)            |  [Screenshot](readme-images/testing/browser/chrome-remove-all.png)             |[Screenshot](readme-images/testing/browser/moz-remove-all.png)         | No issues |
|Menu-filter Gluten Free  | [Screenshot](readme-images/testing/browser/edge-gf-filter.png)             |  [Screenshot](readme-images/testing/browser/chrome-gf-filter.png)              |[Screenshot](readme-images/testing/browser/moz-gf-filter.png)          | No issues |
|Menu-filter Veg          | [Screenshot](readme-images/testing/browser/edge-veg-options.png)           |  [Screenshot](readme-images/testing/browser/chrome-veg-options.png)            |[Screenshot](readme-images/testing/browser/moz-veg-filter.png)         | No issues |
|Menu-filter Veg and GF   | [Screenshot](readme-images/testing/browser/edge-veg-gf-options.png)        |  [Screenshot](readme-images/testing/browser/chrome-veg-gf-options.png)         |[Screenshot](readme-images/testing/browser/moz-veg-gf.png)             | No issues |
|Menu-filter option needed| [Screenshot](readme-images/testing/browser/edge-option-missing.png)        |  [Screenshot](readme-images/testing/browser/chrome-option-missing.png)         |[Screenshot](readme-images/testing/browser/moz-option-missing.png)     | No issues |
|Menu-filter all shown    | [Screenshot](readme-images/testing/browser/edge-filter-show-all.png)       |  [Screenshot](readme-images/testing/browser/chrome-filter-show-all.png)        |[Screenshot](readme-images/testing/browser/moz-filter-show-all.png)    | No issues |
|Menu-update item selected| [Screenshot](readme-images/testing/browser/edge-update-item.png)           |  [Screenshot](readme-images/testing/browser/chrome-update-item.png)            |[Screenshot](readme-images/testing/browser/moz-update-item.png)        | No issues |
|Menu-update updated      | [Screenshot](readme-images/testing/browser/edge-updated.png)               |  [Screenshot](readme-images/testing/browser/chrome-updated.png)                |[Screenshot](readme-images/testing/browser/moz-item-updated.png)       | No issues |
|Menu-add item            | [Screenshot](readme-images/testing/browser/edge-add-item.png)              |  [Screenshot](readme-images/testing/browser/chrome-add-item.png)               |[Screenshot](readme-images/testing/browser/moz-add-item.png)           | No issues |
|Menu-item added          | [Screenshot](readme-images/testing/browser/edge-item-added.png)            |  [Screenshot](readme-images/testing/browser/chrome-item-added.png)             |[Screenshot](readme-images/testing/browser/moz-item-added.png)         | No issues |
|Menu-delete selected     | [Screenshot](readme-images/testing/browser/edge-delete-selected.png)       |  [Screenshot](readme-images/testing/browser/chrome-delete-selected.png)        |[Screenshot](readme-images/testing/browser/moz-delete-selected.png)    | No issues |
|Menu-deleted             | [Screenshot](readme-images/testing/browser/edge-deleted.png)               |  [Screenshot](readme-images/testing/browser/chrome-deleted.png)                |[Screenshot](readme-images/testing/browser/moz-deleted.png)            | No issues |
|Checkout                 | [Screenshot](readme-images/testing/browser/edge-checkout.png)              |  [Screenshot](readme-images/testing/browser/chrome-checkout.png)               |[Screenshot](readme-images/testing/browser/moz-checkout.png)           | No issues |
|Checkout- success        | [Screenshot](readme-images/testing/browser/edge-order-success.png)         |  [Screenshot](readme-images/testing/browser/chrome-order-success.png)          |[Screenshot](readme-images/testing/browser/moz-order-success.png)      | No issues |
|My Orders                | [Screenshot](readme-images/testing/browser/edge-myorders.png)              |  [Screenshot](readme-images/testing/browser/chrome-myorders.png)               |[Screenshot](readme-images/testing/browser/moz-my-orders.png)          | No issues |
|All Orders               | [Screenshot](readme-images/testing/browser/edge-all-orders.png)            |  [Screenshot](readme-images/testing/browser/chrome-all-orders.png)             |[Screenshot](readme-images/testing/browser/moz-all-orders.png)         | No issues |
|About us                 | [Screenshot](readme-images/testing/browser/edge-about-us.png)              |  [Screenshot](readme-images/testing/browser/chrome-about-us.png)               |[Screenshot](readme-images/testing/browser/moz-about-us.png)           | No issues |
|404                      | [Screenshot](readme-images/testing/browser/edge-404.png)                   |  [Screenshot](readme-images/testing/browser/chrome-404.png)                    |[Screenshot](readme-images/testing/browser/moz-404.png)                | No issues |

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Responsiveness and performance Testing

In addition to the desktop testing above, the site has also been tested on the following physical devices:
- Mobile: Samsung A32 5g
- Tablet: Apple iPad 10th gen

The results from the testing are tabulated below:


| Page                    | Mobile                                                                     | Tablet                                                                         | Outcome    | 
| ------------------------| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------|------------|
|Register                 | [Screenshot](readme-images/testing/device/mobile-register.png)             | [Screenshot](readme-images/testing/device/ipad-register.png)                   | No Issues  |
|Login                    | [Screenshot](readme-images/testing/device/mobile-login.png)                | [Screenshot](readme-images/testing/device/ipad-login.png)                      | No Issues  |
|Logout                   | [Screenshot](readme-images/testing/device/mobile-logout.png)               | [Screenshot](readme-images/testing/device/ipad-logout.png)                     | No Issues  |
|Home                     | [Screenshot](readme-images/testing/device/mobile-home.png)                 | [Screenshot](readme-images/testing/device/ipad-home.png)                       | No Issues  |
|Menu                     | [Screenshot](readme-images/testing/device/mobile-menu.png)                 | [Screenshot](readme-images/testing/device/ipad-menu.png)                       | No Issues  |
|Menu-item details        | [Screenshot](readme-images/testing/device/menu-item-details.png)           | [Screenshot](readme-images/testing/device/ipad-menu-details.png)               | No Issues  |
|Menu - add to cart       | [Screenshot](readme-images/testing/device/menu-add-to-cart.png)            | [Screenshot](readme-images/testing/device/ipad-add-to-cart.png)                | No Issues  |
|Menu-increase quantity   | [Screenshot](readme-images/testing/device/menu-add-to-cart.png)            | [Screenshot](readme-images/testing/device/ipad-increase-qty.png)               | No Issues  |
|Menu- decrease quantity  | [Screenshot](readme-images/testing/device/mobile-decrease-qty.png)         | [Screenshot](readme-images/testing/device/ipad-decrease-qty.png)               | No Issues  |
|Menu - max quantity      | [Screenshot](readme-images/testing/device/mobile-max-qty.png)              | [Screenshot](readme-images/testing/device/ipad-max-qty.png)                    | No Issues  |
|Menu - remove all        | [Screenshot](readme-images/testing/device/mobile-remove-all.png)           | [Screenshot](readme-images/testing/device/ipad-empty-cart.png)                 | No Issues  |
|Menu-filter Gluten Free  | [Screenshot](readme-images/testing/device/mobile-gf-options.png)           | [Screenshot](readme-images/testing/device/ipad-gf-options.png)                 | No Issues  |
|Menu-filter Veg          | [Screenshot](readme-images/testing/device/mobile-veg-options.png)          | [Screenshot](readme-images/testing/device/ipad-veg-options-shown.png)          | No Issues  |
|Menu-filter Veg and GF   | [Screenshot](readme-images/testing/device/mobile-veg-gf-options.png)       | [Screenshot](readme-images/testing/device/ipad-veg-gf-shown.png)               | No Issues  |
|Menu-filter option needed| [Screenshot](readme-images/testing/device/mobile-option-needed.png)        | [Screenshot](readme-images/testing/device/ipad-filter-make-selection.png)      | No Issues  |
|Menu-filter all shown    | [Screenshot](readme-images/testing/device/mobile-all-options-shown.png)    | [Screenshot](readme-images/testing/device/ipad-filter-all.png)                 | No Issues  |
|Menu-update item selected| [Screenshot](readme-images/testing/device/mobile-update-item.png)          | [Screenshot](readme-images/testing/device/ipad-update-item.png)                | No Issues  |
|Menu -update updated     | [Screenshot](readme-images/testing/device/mobile-item-updated.png)         | [Screenshot](readme-images/testing/device/ipad-item-updated.png)               | No Issues  |
|Menu - add item          | [Screenshot](readme-images/testing/device/mobile-add-item.png)             | [Screenshot](readme-images/testing/device/ipad-add-item.png)                   | No Issues  |
|Menu - item added        | [Screenshot](readme-images/testing/device/mobile-item-added.png)           | [Screenshot](readme-images/testing/device/ipad-item-added.png)                 | No Issues  |
|Menu - delete selected   | [Screenshot](readme-images/testing/device/mobile-delete-selected.png)      | [Screenshot](readme-images/testing/device/ipad-delete-selected.png)            | No Issues  |
|Menu - deleted           | [Screenshot](readme-images/testing/device/mobile-item-deleted.png)         | [Screenshot](readme-images/testing/device/ipad-item-deleted.png)               | No Issues  |
|Checkout                 | [Screenshot](readme-images/testing/device/mobile-checkout.png)             | [Screenshot](readme-images/testing/device/ipad-checkout.png)                   | No Issues  |
|Checkout - success       | [Screenshot](readme-images/testing/device/mobile-checkout-success.png)     | [Screenshot](readme-images/testing/device/ipad-checkout-success.png)           | No Issues  |
|My Orders                | [Screenshot](readme-images/testing/device/mobile-my-orders.png)            | [Screenshot](readme-images/testing/device/ipad-myorders.png)                   | No Issues  |
|All Orders               | [Screenshot](readme-images/testing/device/mobiles-allorders.png)           | [Screenshot](readme-images/testing/device/ipad-allorders.png)                  | No Issues  |
|About us                 | [Screenshot](readme-images/testing/device/mobile-about-us.png)             | [Screenshot](readme-images/testing/device/ipad-aboutus.png)                    | No Issues  |
|404                      | [Screenshot](readme-images/testing/device/mobile-404.png)                  | [Screenshot](readme-images/testing/device/ipad-404.png)                        | No Issues  |


## Defence programming Testing
come back to

## User story testing?
link in images?

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Manual Testing

In addition to all the testing above, the following extensivee manual testing has been carried out checking each element of the site as a whole entity. The results have been tabulated below:

| Test  | Test Step                                                           |Expected Result                            |              Actual Result                                                                  | Screenshot                                                   | Outcome | 
| ------|:--------------------------------------------------------------------|----------------------------------------   | --------------------------------------------------------------------------------------------|--------------------------------------------------------------|:-------:|
|MT1    | Navigation: Menu                                                    | Navigates to the menu page                | As Expected                                                                                 |[Screenshot](readme-images/testing/manual/mt-fullmenu.png)    | Pass    |
|MT2    | Navigation: Access the site                                         | Navigate to the site, site loads          | As Expected                                                                                 |[Screenshot](readme-images/testing/manual/mt-siteloads.png)   | Pass    |
|MT3    | Navigation: About us                                                | Navigates to the about us page            | As Expected                                                                                 |[Screenshot](readme-images/testing/manual/mt-aboutus.png)     | Pass    |
|MT4    | Navigation: Register                                                | Navigates to the registration page        | As Expected                                                                                 |[Screenshot](readme-images/testing/manual/mt-registration.png)| Pass    |
|MT5    | Navigation: Login                                                   | Navigates to the login page               | As Expected                                                                                 |[Screenshot](readme-images/testing/manual/mt-login-page.png)  | Pass    |
|MT6    | Footer Navigation: Facebook                                         | Navigates to the facebook homepage        | As Expected                                                                                 |[Screenshot](readme-images/testing/manual/mt-facebook.png)    | Pass    |
|MT7    | Footer Navigation: X                                                | Navigates to the X homepage               | As Expected                                                                                 |[Screenshot](readme-images/testing/manual/mt-X.png)           | Pass    |
|MT8    | Footer Navigation: Instagram                                        | Navigates to the Instagram homepage       | As Expected                                                                                 |[Screenshot](readme-images/testing/manual/mt-insta.png)       | Pass    |
|MT9    | Footer Navigation: Youtube                                          | Navigates to the Youtube homepage         | As Expected                                                                                 |[Screenshot](readme-images/testing/manual/mt-youtube.png)     | Pass    |
|MT10   | Menu: menu loads                                                    | Full active menu can be seen              | Full menu available to see                                                                  |[Screenshot](readme-images/testing/manual/mt-fullmenu.png)    | Pass    |    
|MT11   | Menu: Items                                                         | Menu items available in sections          | Broken down into Deals, Pizzas, Sides, Drinks, Desserts for ease.                           |[Screenshot](readme-images/testing/manual/mt-fullmenu.png)    | Pass    |
|MT12   | Menu: Layout                                                        | Menu layout is easy to follow             | Layout easy to follow, consistent                                                           |[Screenshot](readme-images/testing/manual/mt-fullmenu.png)    | Pass    |
|MT13   | Menu: Item information                                              | Items have information available          | Items appropriately named with descriptions and allergen info                               |[Screenshot](readme-images/testing/manual/mt-item-info.png)   | Pass    |
|MT14   | Menu: Filter Veg Options                                            | Menu should filter and show veg only      | Filtered to show Veg options only. Notification given.                                      |[Screenshot](readme-images/testing/manual/mt-vegonly.png)     | Pass    |
|MT15   | Menu: Filter GF Options                                             | Menu should filter and show GF only       | Filtered to show GF options only. Notification given.                                       |[Screenshot](readme-images/testing//manual/mt-gfonly.png)     | Pass    |
|MT16   | Menu: filter GF and Veg Options                                     | Filter to show Veg and GF options only    | Filter to show veg and GF only. Notification given.                                         |[Screenshot](readme-images/testing/manual/mt-vegandgf.png)    | Pass    |
|MT17   | Menu: Remove allergen filter                                        | Filter should be removed showing all      | Filtered removed, shows all. Notification given                                             |[Screenshot](readme-images/testing/manual/mt-alloptions.png)  | Pass    |
|MT18   | Menu: Filter no selection, filter applied                           | User notfied as such, asked to correct    | Notification given: Please select an option first                                           |[Screenshot](readme-images/testing/manual/mt-filtererror.png) | Pass    |
|MT19   | Menu: item details                                                  | Clicking view item details are visible    | Bootstrap modal opened: Item information given. Option to add to basked or close modal      |[Screenshot](readme-images/testing/manual/mt-iteminfo.png)    | Pass    |
|MT20   | Menu: item details – close/navigate back                            | Navigates back to the menu page           | Modal closed using X or close button. Menu returned into view                               | as MT10                                                      | Pass    |
|MT21   | Menu: Add to cart                                                   |  User can added item/quantity to cart     | Selected item/quantity added to cart. Notification given                                    |[Screenshot](readme-images/testing/manual/mt-addedtocart.png) | Pass    |
|MT22   | Menu: Add to cart: 0 quantity                                       | User to be advised of minimum quantity    | Alert provided: Value must be greather than or equal to 1                                   |[Screenshot](readme-images/testing/manual/mt-addzero.png)     | Pass    |
|MT23   | Menu: View item, update quantity                                    | The selected item quantity should update  | Quantity updated. Notification given. New quantity seen in cart                             |[Screenshot](readme-images/testing/manual/mt-updateqty.png)   | Pass    |
|MT24   | Cart: Information                                                   | Cart reflects total items and total       | As expected. Cart updates dynamically.                                                      | As MT21 or MT22                                              | Pass    |
|MT25   | Cart: Increase quantity                                             | Should increase, totals should update     | As expected. Notification given                                                             |[Screenshot](readme-images/testing/manual/mt-cart-add.png)    | Pass    |
|MT26   | Cart: Decrease quantity                                             | Should decrease, totals should update     | As expected. Notification given                                                             |[Screenshot](readme-images/testing/manual/mt-cart-decrease.png)|Pass    |
|MT27   | Cart: Decrease quantity < 1                                         | Item removed if quantity is 0 in cart     | As expected, notification given                                                             |[Screenshot](readme-images/testing//manual/mt-cartqty-0.png)  | Pass    |
|MT28   | Cart: Increase quantity > 10                      | User informed of maximum allowed          | Notification given: Max quantity of 10 allowed. Cart values unchanged.                                        |[Screenshot](readme-images/testing/manual/mt-cart-max.png)    | Pass    |
|MT29   | Navigation: Checkout                              | Navigation from cart takes the user to checkout page.       | As Expected.                                                                                |[Screenshot](readme-images/testing/manual/mt-checkout.png)    | Pass    |
|MT30   | Checkout: Details                                 |Order for available with order summary.                      | As Expected.                                                                                | As MT29                                                      | Pass    |
|MT31   | Checkout: "Pay" on empty form                     | The site should't process the order                         | Pay button disable till required fields filled.                                             | As MT29                                                      | Pass    |
|MT32   | Checkout: Enter invalid card number               | User is notified of error                                   | User notified card is invalid                                                               |[Screenshot](readme-images/testing/manual/mt-card-invalid.png)| Pass    |
|MT33   | Checkout: Invalid card :mm/yy                     | User is notified of the error                               | User notified mm/yy is invalid                                                              |[Screenshot](readme-images/testing/manual/mt-carmmyy-invalid.png)| Pass |
|MT34   | Checkout: Valid payment info                      | Able to proceed to next step/pay                            | Pay button now enabled                                                                      |[Screenshot](readme-images/testing/manual/mt-validpayment.png) |  Pass  |
|MT35   | Checkout: Form name missing                       | User should be notified                                     | Prompt given to correct                                                                     |[Screenshot](readme-images/testing/manual/mt-name-error.png)  | Pass    |
|MT36   | Checkout: Form phone missing                      | User should be notified                                     | Prompt given to correct                                                                     |[Screenshot](readme-images/testing/manual/mt-phone-error.png) | Pass    |
|MT37   | Checkout : Form Email missing                     | User should be notified                                     | Prompt given to correct                                                                     |[Screenshot](readme-images/testing/manual/mt-email-error.png) | Pass    |
|MT38   | Checkout: Form billing name missing               | User should be notified                                     | Prompt given to correct                                                                     |[Screenshot](readme-images/testing/manual/mt-billing-err.png) | Pass    |
|MT39   | Checkout: Form address 1 missing                  | User should be notified                                     | Prompt given to correct                                                                     |[Screenshot](readme-images/testing/manual/mt-add-error.png)   | Pass    |
|MT40   | Checkout: Form town is missing                    | User should be notified                                     | Prompt given to correct                                                                     |[Screenshot](readme-images/testing/manual/mt-town-err.png)    | Pass    |
|MT41   | Checkout: Form Postcode missing                   | User should be notified                                     | Prompt given to correct                                                                     |[Screenshot](readme-images/testing/manual/mt-postcode-err.png)| Pass    |
|MT42   | Checkout: Pay, Order confirmation                 | Order proccessed, confirmation given to user                | As Expected                                                                                 |[Screenshot](readme-images/testing/manual/mt-order-conf.png)  | Pass    |
|MT43   | Checkout: confirmation email sent/recieved        | Order confirmation emailed to user                          | Confirmation recieved                                                                       |[Screenshot](readme-images/testing/manual/mt-order-conf.png)  | Pass    |

> [!NOTE]
> Return back to the [README.md](README.md) file.


## Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Anaveednaseem84%2FPP5-Ds_Pizza%20label%3Abug&label=bugs)](https://www.github.com/naveednaseem84/PP5-Ds_Pizza/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

 [GitHub Issues](https://www.github.com/naveednaseem84/PP5-Ds_Pizza/issues) has actively been used to track and manage bugs and issues during the development stages of my project. 

 A summary of the bugs is available below:

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


> [!IMPORTANT]
As far as I am aware there are no remaing bugs. I have endeavoured to throughly test the site but am unable to completely rule out the possibility of any arising in the future.

> [!NOTE]
> Return back to the [README.md](README.md) file.




