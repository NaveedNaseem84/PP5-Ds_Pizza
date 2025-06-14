# D's Pizza using Django, Python and Postgres.

## Introduction

Welcome to D's pizza - a family run local business, serving the food fanatics for many years. The site proudly presents hand crafted pizzas, perfected with locally sourced ingredients, with our secret tomato sauce on our home made dough.

In addition to yummy (as reviewed!) pizza's, the site offers combo deals which include a pizza, side, drink and a dessert at a value for money price. Whether the customer wants to grab a quick pizza or a family wanted to grab a complete meal, we accomodate for all. 

The intention of the site is to provide the user with a smooth user experience whilst they browse the menu and deals on offer, add items to the cart and place orders via the quick checkout process provided. Regardless of the device used, the performance and usability is maintained through out providing a positive user experience. Potential users of site include regular customers, students wanting best value for money, working proffessionals where time is of the essence or families who want to get the complete meal in a quick and easy way.


## Table of Contents

### User Experience (UX)

* User Stories

* Mind Map: Ideas

* Wireframe Designs 

* UX View

* Pseudo - functions needed (Brainstorm)

### Structure and Processes

* Process Map

* E-commerce Business Model

* Models and Entity Relationship Diagrams (ERD's)

### Search Engine Optimisation

### Marketing

### Project Walkthrough

### Testing

* Fixed Bugs 

* Validation Testing

* Functionality/performance testing

* Manual Testing

* Automated Testing

* User Story Testing 

### Future Developments

###  Workload Planning

###   Site Production, Deployment and Contribution

 * Site production

 * Deployment

 * Contribution

### Technologies and tools Used

* Languages used

* Frameworks, Libraries and Programs Used
     	
### Credits

* Content

* General
  
* Overall Credit

### Personal Summary

## User Experience (UX)
### User Stories

The first step taken was to the establish the user stories identifying the needs and requirements for the site. These have further provided the foundation for the project allowing me to categorise the development and deployment using agile methodology.

Each user story below has the initial story along with acceptance criteria. These both would need be satisfied during development, testing and deployment for the user story to be considered a success.

### **US1:** As a **Customer** I can **I can add items to the cart** so that **I can review/buy them**
#### Acceptance Criteria
-  Items are available to add to the cart
-  Items with selected quantity are added to the cart
-  A notification is displayed when this occurs
-  The cart displays the quantity total, item total and a grand total for cart
-  Item quantities can be increased from within the cart
-  The cart persists across the site

### **US2:** As a **Customer** I can **remove items from the cart** so that **I can adjust the amount needed**
#### Acceptance Criteria
- The selected item quantity is reduced from the cart
- A notification is displayed when this occurs
- The cart is updated to reflect the change
- The item is completely removed from the cart if the quantity is 0

### **US3:** As a **Customer** I can **proceed to the checkout** so that **I can place the order**
#### Acceptance Criteria
- The checkout provides the customer a summary of the cart
- A form is shown requiring a name, email and phone number which is validated accordingly.
- The option to pay by card is available to the customer

### **US4:** As a **Customer** I can **see order confirmation** so that **I know the order has been placed**
#### Acceptance Criteria
- A confirmation page is displayed with the order number and other relevant information once the payment has been processed successfully 
- The order is saved within the database
- An error page displayed should the payment fail

### **US5:** As a **Customer** I can **save an order as a favourite repeat item** so that **easily re-order in the future**
#### Acceptance Criteria
- An option is given on the confirmation page to add to favourites
- A favourites section is available showing all the favourite items marked as so
- Only the logged in users can see this facility

### **US6:** As a **Customer** I can **access the site on multiple devices** so that **I can view/order when it suits** - *OPTIONAL*
#### Acceptance Criteria
- The site is fully responsive across desktop and mobile devices with no loss in performance or functionality
- The UI scales smoothly across devices

### **US7:** As a **Customer** I can **see the complete menu** so that **I can decide If/what I want to order**
#### Acceptance Criteria
- The customer can see the complete menu: Deals, Pizza and Extras
- Any additional product information such as toppings is available to see
- All the information shown is in a clear readable format

### **US8:** As a **Customer** I can **see deals clearly** so that **I can order a complete meal in one go**
#### Acceptance Criteria
- The deals are available in a section of their own 
- Complete descriptions of the items within the deal are available

### **US9:** As a **Customer** I can **see dietary/allergen information clearly** so that **I can make an informed decision when ordering**
#### Acceptance Criteria
- Allergen information is shown on relevant items
- Items can be filtered by dietary needs.

### **US10:** As a **Customer** I can **toggle between light/dark mode** so that **it matches my view preference** *-OPTIONAL*
#### Acceptance Criteria
- A simple toggle that allows the change from dark to light and vice versa

### **US11:** As a **admin** I can **add new products** so that **they are available on the menu**
#### Acceptance Criteria
- A form is made available to add the product after validation
- Once saved, the product is shown on the menu real time

### **US12:** As an **Admin** I can **see all the orders** so that **I can aid fulfilment**
#### Acceptance Criteria
- The admin is authenticated as having access to the dashboard
- Orders can be filtered and updated by status i.e. ordered, preparing or ready.

### **US13:** As an **Admin** I can **update products** so that **they always contain the latest information**
#### Acceptance Criteria
- A pre-filled form is made available on the selected product
- Any updates are validated
- The product is updated, notification displayed, and the changes shown dynamically

### **US14:** As an **admin** I can **remove products** so that **they are no longer on the menu**
#### Acceptance Criteria
- A delete option is available
- A confirmation is requested for the delete
- The Item is removed from the DB once confirmed

### **US15:** As a **Admin** I can **see sales statistics** so that **can evaluate best/worst sellers** - *OPTIONAL*
#### Acceptance Criteria
- An dashboard available showing real time sale statistics
- Dashboard is filterable on different products/days

Once the user stories had been establised, they were broken down into three milestones within the project:

- MVP Release: Order Flow - the minimum viable product to fulfill the basic requirements.
- User Experience - Enchancing the MVP to give the users a positive user experience on all aspects of the site.
- Product administration - This milestone primarily has the focus of ensuring that any new products, product updates or removals can effectively be carried out allowing the business to run in a streamlined way. 

The user stories above have been placed in the milestones above and have been priortised using the MoSCow priortisation technique allowing the focus on essential features and further making informed decisions on what else could be potentially be included in the final product.


[Back to Contents.](#table-of-contents)

### Mind Maps : Ideas

The proceeding step was to take a simple pen to paper approach to capture a high level view of the functionality required from the site. The purpose of this was to initiate the thought process on how the user stories above could be implemented:

![Mindmap](readme-images/process_map.jpeg)


### Wireframe Designs

The next step was to create the wireframes (shown below) using Balsamiq. These wireframes serve the purpose to illustrate the planned layouts and components to help fulfill the user stories.

![home/index](readme-images/wireframes/1_home.png)

![menu](readme-images/wireframes/2_menu.png)

![product_detail](readme-images/wireframes/3_product_detail.png)

![cart](readme-images/wireframes/4_cart.png)

![checkout_invalid](readme-images/wireframes/5_Checkout_invalid_payment.png)

![checkout_success](readme-images/wireframes/6_Checkout_payment_order_success.png)

![admin_menu](readme-images/wireframes/7_Admin_Menu.png)

![admin_update](readme-images/wireframes/8_Admin_Menu-update_item.png)

![admin_add](readme-images/wireframes/9_Admin_Menu_Add_item.png)

![admin_delete](readme-images/wireframes/10_Admin_Menu-Delete_item.png)

![management_dashboard](readme-images/wireframes/11_Management_Dashboard.png)

![sign_in](readme-images/wireframes/12_Sign_in.png)

![register](readme-images/wireframes/13_Register.png)

![logout](readme-images/wireframes/14_Logout.png)

[Back to Contents.](#table-of-contents)

### UX View

Following on from the wireframe designs, final UX views of the site were created:

![home](readme-images/UX/1_home.png)

![menu](readme-images/UX/2_menu.png)

![product_detail](readme-images/UX/3_product_detail.png)

![add_to_cart](readme-images/UX/4_add_to_cart.png)

![cart_summary](readme-images/UX/5_cart_summary.png)

![checkout](readme-images/UX/6_checkout.png)

![aboutus](readme-images/UX/10_aboutus.png)

![menu_admin](readme-images/UX/7_menu_admin.png)

![order_dashboard](readme-images/UX/8_order_dashboard.png)

![register_login_logout](readme-images/UX/9_register_login_logout.png)

The combination of the wireframes and UX renders of the site have provided a clear picture for the final product. The defintion of colours, classes, placements, and components will act as the reference guide during the course of development to ensure a positive user experience whilst providing the required functionality.

[Back to Contents.](#table-of-contents)


### Pseudo - functions needed (Brainstorm)

The completion of the UX element provided food for thought, and the next step was to brainstorm the potential functions for the customer to order and the admin to maintain the products.

As a customer:

![customer](readme-images/pseudo_customer.jpeg)

As a admin/superuser:

![customer](readme-images/pseudo_admin.jpeg)

## Structures and Processes

### Process Maps

The diagrams below illustrate the process flow taken by the respected actions and the outcome achieved after any necessary validation:

Add/delete/update an item:

![add_delete_update](readme-images/process_maps/add_delete_update.png)

Add item to cart:

![add_to_cart](readme-images/process_maps/add_to_cart.png)

Remove from cart:

![remove_from_cart](readme-images/process_maps/remove_reduce.png)


These process maps have played an essential part as a reference guide during the development. They have allowed me to ensure that  requirements and acceptance criteria from the user stories have been satisfied.

### E-commerce Business Model

The site requires the user to select a pizza or deal, pay for it, receive confirmation of this order so that the business can proceed to make the food items on the order.

This classifies the site as an e-commerce application as it facilitates business transactions with the transfer of product, user and financial information online resulting in fulfilment of the transaction. The user is able to freely decide what they want to purchase and how they would like to pay for it without needing any approval or direction.

The e-commerce application falls under the category type of a **Business to Customer (B2C)** with the following criteria:

- A physical product is being sold and provides the following information:
  - Product name – pizza: Mexicana Cheese pizza
  - Clear description – toppings contained on the pizza
  - Any other information: gluten free and/or suitable for vegetarian 
  - Price – cost of the item

- Features:
  - Ability to filter results
  - Cart and payment system
  - Notifications of when item is added to or removed from a basket
  - Notifications of sucessful order
 
- Payment:
  - single payment taken for the product(s)
  - Confirmation of the order
  - Transaction complete as a “one time service”

### Models and Entity Relationship Diagrams (ERD's)

The project on a whole contains four models:

1. Pizza -  for the Pizza products
2. Deal - for the Deal products
3. Extras - for the extras: sides, drinks and desserts
4. Order - the confirmed order placed (contains line items)
5. OrderLineItem - the items contained within the order(4)

#### 1. Pizza

The Pizza model contains the following setup:

 - name: the name of the pizza
 - description: the toppings on the pizza
 - active: whether the pizza is active or not ( choices: yes/no)
 - is_gf: if the pizza is gluten free
 - is_veg: if the pizza is vegetarian
 - price: the cost of the item

 The ERD schema for the Pizza model is as follows:

 ![erd_pizza](readme-images/erds/erd_pizza.png)

 #### 2. Deal

 The Deal model contains the following setup:

 - name: the name of the deal
 - pizza: the pizza in the deal from the pizza model*
 - side: the side in the deal from the extra model*
 - drink: the drink in the deal from the extra model*
 - dessert: the dessert in the deal from the extra model*
 - price: the cost of the deal
 - active: whether the deal is active or not (choices: yes/no)

* the associated items need to be active within their models to be a part of this deal. If they were to be deleted/made inactive the logic would assume that the deal would no longer be running.

 The ERD schema for the Deal model is as follows:

  ![erd_deal](readme-images/erds/erd_deal.png)

#### 3. Extras

The Extras model contains the following setup:

- name: the name of the extra
- description: description of the item if applicable
- category: the item is required to sit in a choice: Side, Drink or Dessert
- active: whether the deal is active or not(choices: yes/no)
- price: the cost of the item

 The ERD schema for the Extras model is as follows:

  ![erd_extra](readme-images/erds/erd_extras.png)

 #### 4. PizzaOrder

 The Pizza Order model contains the following setup:

 - order_ref: reference for the order which is generated automatically when the order is created
 - name: the name for the order
 - user: an optional field which is automatically filled when a logged in user makes the order
 - phone: the phone number associated with the order
 - email: the email associated with the order
 - billing_name: name of the individual making the payment
 - address_line_1: *
 - address_line_2: *
 - town: *
 - postcode: *
 - date: date/time of the order
 - order_total: total of the order
 - status: the status of the order. By default is set to "ordered" when the order is created

 *bill payers address information


#### 5. OrderLineItem

The Order Line Item contains the following setup:

- order: a Foreign key to the Pizza Order model above tying the line items to that specific order
- product: the product on the paticular line
- price: the price per unit of the item
- quantity: the quantity ordered
- line_total: a total of the line items 

The ERD schema for the Pizza Order and OrderLineItem models is as follows:

![erd_order](readme-images/erds/erd_pizzaorder_and_lineitems1.png)

[Back to Contents.](#table-of-contents)

## Search Engine Optimisation

From an e-commerce business pespective, search engine optimisation (SEO) techniques have been utlised to firstly ensure that the site is targeted towards its intended audience and secondly its ranked highly enough in search results.

The intial step taken was to brainstorm potential keywords (both short and longtail) for the pizza business. The thought process behind these keywords has been to simply pace myself in the shoes of customer searching for pizza.

The results of the brain storm as follows:

| Shortail words          |      Long tail words              |
|:----------------------- |:----------------------------------|
| Pizza                   |Hand crafted Pizzas                |
| Pizza near me           |Pizzas in Manchester               |
| Fresh Pizza             |Pizza Near Me                      |
| Woodfire pizza          |Gluten-Free pizza near me          |
| Order pizza             |Popular pizza deals                |
| Local pizza             |Fresh Artisan Pizza Manchester     |
| Artisan pizza           |Pizza collection open now near me  |
| Fresh pizza             |                                   |
| Pizza Manchester        |                                   |
| Pizza Deals             |                                   |
| Pizza for collection    |                                   |
| Good pizza manchester   |                                   |

Carrying out a quick google search of the words above found that certain words seemed to get lost within the search results such as "order pizza" or "local pizza". This would not be ideal as the site would sit side by side with it's potential competitors. 

### SEO Implementation: HTML

To maximise the posibility of the site being returned in the search results, it was decided to use the following key words on the landing page:

```HTML
 <h2>Artisan Pizza</h2>

<h3>Hand crafted pizzas in Manchester</h3>

  <h4> New: Gluten free pizza options</h4>

  <h> semantics tags have been used so they can be picked as a priority over other elements. 
```

### SEO Implementation: Meta data

To further increase reach of the site, the following was adding as meta data:

- `description`: "Ds Pizza in Manchester, providing fresh, local, popular pizzas and deals for collection"

- `keywords`: "love food, artisan pizza, woodfire pizza, local pizza, food deals, pizza deals,
        pizza manchester, pizza near me, pizza for collection, Good pizza manchester"

[Back to Contents.](#table-of-contents)
## Marketing

As D's pizza is a startup business, and in order to keep costs to a minimum, organic marketing has been opted as the preferred choice to help the brand expand on social media. 

After considering which strategies will work effectively for the e-commerce site, the stategies chosen are:

- Email marketing
- Facebook

These two strategies have been chosen based on the types of uses and how the service is available - online. 

The email marketing option allows for the business to send out marketing information such as new deals or voucher codes which the user can use to obtain discounts. In order to comply with GDPR, this option would allow the user to subscribe to the site with the option to unsubscribe at any time.

The option to use facebook for core marketing means maximum exposure to a platform where the current users are listed as over 3 billion* The process to quickly create posts, snap and update new product photos means that it can be done quickly and effectively.

*Quick google of the statistics.

### Email marketing

Email marketing has been configured via Mail chimp and is up and running to recieve data when a user subscribes via teh website about page, and there already appears to be a keen subscriber:


![mail-chimp-subscriber](readme-images/project-walkthrough/mail-chimp-dashboard.png)

### Facebook

D's pizza is up and runnning on facebook pages:

![ds'-facebook](readme-images/project-walkthrough/ds-facebook-page.png)

The link to the page can be seen at
https://www.facebook.com/profile.php?id=61577146115956#

**Please note** The link above was active at the same of taking the screenshot above.

[Back to Contents.](#table-of-contents)

## Project Walkthrough

#### Introduction

The site provides the flexibility of allowing the users to place an order in two ways:

 - As an anonymous visitor where there is no registration/login required. A valid payment method is required, where on completion the order is placed.
 - As a registered and logged in user.  In addition to the above, the logged in user is able to see the all of their orders in a section within the site which will be demonstrated in this walkthrough.

For the purposes of this project, a *manager* account has been setup with "is staff" permissions so that they can:

- Add any new product to the site.
- Update any current product on the site.
- Delete any product on the site.
- See all the orders made and update their status accordingly.

This *manager* CRUD functionality is carried out fully from the front of the website with *no* need to access the django admin panel.

## Home

On navigation to the site, the user is presented with a crisp layout, in an vibrant colour scheme. Regardless of device, the site scales across smoothly without affecting performance or UX:

![responsive-all-devices](readme-images/project-walkthrough/responsive-all-devices.png)

_**Image above generated using https://ui.dev/amiresponsive illustrating the responsiveness of the site.**_

### Features

#### Navigation

The site features a full responsive navigation menu which is made available throught the site:

![Navbar](readme-images/project-walkthrough/navbar-full.png)

 - The 'Ds' link takes the user back to the home page.
 - The menu and aboutus takes the users to respected pages.
 
Clicking on the 'person' icon next to the about Us link presents a drop down menu:

 ![drop-down-post-login](readme-images/project-walkthrough/drop-down-options-post-login.png)

The drop down options to login or register take the user to the respected pages which will be covered later in this walkthrough.

The cart icon in the far right navigates the user to cart page - currently empty as there are no items added.

The main focal point of the home page draws the user attention to purpose of the company and site:


![index-focal-point](readme-images/project-walkthrough/index-focal-point.png)
The text delivered on the home page implements the keywords chosen as part of the SEO section carried out above. Key placement of the words ensure not only to catch the users eyes, but also return the site amongst search engine searches as a picked option.

#### Footer

Similiar to the nav, bar there is a footer available at the bottom of the screen and is seamlessly across the site:

![footer](readme-images/project-walkthrough/footer.png)

- The footer contains links to the respected social media sites Facebook, X, Instagram, and YouTube using font awesome icons.
- These links are all opened in a new tab.

**Please note:** There are currently no active social media pages for Sultan's. These links have been added in as place holders only.

[Back to Contents.](#table-of-contents)

## Menu

Navigating to the menu page the user is presented with a very flavoursome menu. Displayed in clean, easy to read format, the user can see the deals, pizzas, sides, drinks and desserts currently on offer. 

Where applicable, any allergen information is clearly displayed within the product information.

 There is also a handy cart shown to the right of the screen which dynamically updates when an item is added to the cart:

![menu-main](readme-images/project-walkthrough/menu-main.png)

### Features

#### Allergen filter

A convnienent allergen filter is available, which allows the user to filter the products based on the following requirements:

![allergen-filter](readme-images/project-walkthrough/allergen-filter.png)

Selecting from one of the options will update the menu, and where applicable the filter results shown. 

For example, Veg only options:

![veg-only-option](readme-images/project-walkthrough/veg-only-option.png)

or gluten free options:

![gf-only](readme-images/project-walkthrough/gf-only-option.png)

Selecting all from the filter removes search criteria and returns the menu back to include all the options. For each selection on the allergen menu, a notification is given in the top right corner:

![gf-notification](readme-images/project-walkthrough/gf-notfication.png)


#### Product information

Each product includes where applicable allergen infirmation, name, description, price and the option to view for more details:

![deal](readme-images/project-walkthrough/deal-main.png)

Selecting "view" on the product, a boostrap modal popup is presented providing further details of the selected product with the option to add the specified quantity to the cart. For convinience, the minimum quantity has been preset to 1:

![deal-detail](readme-images/project-walkthrough/deal-detail.png)

Clicking on the close button will simply close the product information modal bringing the menu back to view.

[Back to Contents.](#table-of-contents)

#### Add to Cart

**Please note** : For the purposes of the project, and to enforce defensive design, the maximum quantity allowed in the cart for a item is 10. In a real world application this would most likely be set by the product owner.

Once the an item has been selected to add to the cart, the quantity specified and the add button clicked, the item is added to the cart and can be seen in the cart overview on the right. A notification is also given that the item has been added, and the cart total shown on the nav bar:

![add-to-cart](readme-images/project-walkthrough/add-to-cart.png)


Once added to the sticky cart, the user has the convinience of increasing/decrease the quantity of the selected item in the cart with a single click.

On increase, the amount is updated and a notification given:

![sticky-cart-increase](readme-images/project-walkthrough/sticky-cart-increase.png)

On decrease, again the amount is updated and a notifcation given:

![sticky-cart-decrease](readme-images/project-walkthrough/sticky-cart-decrease.png)

Should the item quantity already be 10 within the sticky cart, on trying to increase further a notification is displayed:

![sticky-cart-maximum](readme-images/project-walkthrough/sticky-cart-max-qty.png)

The same applies for when the product is being added/updated via the "view" product option. If the quantity is more than 10 as a new item or the new quantity plus the cart quantity of the item is 10, the notification above is given.

On adding/removing/decreasing products from the sticky cart, the grand total and total items within the bag is updated dynamically to always provided the latest figures.
If all the items have been removed, the sticky cart will show as empty and the grand total in the nav bar as zero:

![empty-sticky-cart](readme-images/project-walkthrough/empty-sticky-cart.png)

To access the cart in mobile view, simple select 3 line toggle located to the top right of the screen and select the cart icon:

![mobile-cart](readme-images/project-walkthrough/mobile-cart.png)

Once selected, the cart is displayed. The functionality to increase/decrease items within the cart is done in the same way as sticky cart along with the dynamic update of teh item total and grand total. Once the cart is empty, the user is notified and provided a link to handy link to navigate back to the menu page:

![mobile-cart-empty](readme-images/project-walkthrough/mobile-cart-empty.png)

**Please Note**: This mobile cart can also be accessed on a desktop version. The sticky cart has been placed on the same page for convinience to improve the user experience and reduce the need to navigate forward and back once items have been added/removed.

[Back to Contents.](#table-of-contents)

#### Checkout

Once the user has finalised the cart the user has the option to navigate to the checkout either by using the "pay" link from the stick cart or the "checkout" link on the cart page and is presented with the following:

![checkout-page](readme-images/project-walkthrough/checkout-page.png)

The checkout pages provides order summary listing out all the items in the cart at the time of checkout out. In addition to this, there is also the total number of items and a grand total that is the amount to be used at the time of check out.

For convinience, there is also the option to "add items" which would navigate the user back to the menu page.

To sucessfully checkout the displayed form would need to be filled. The fields present on the form include:

- Name: name for the order - required field
- Phone: validated to have a maximum of 11 numbers only - required field
- Email: correct email syntax - required field
- Billing name: Name of the person paying for the order - required field
- Address line 1: Address of bill payer - required field
- Address line 2: as above, optional
- Town: required field
- Postcode: required field

The final section on check out page is to include a valid (stripe) card number, expiry and CVC. Should any of these be invalid, the user is notified accordingly:

![card-expired](readme-images/project-walkthrough/card-expired.png)

![card-invalid](readme-images/project-walkthrough/card-invalid.png)

If any of the required fields on the main form are incorrect or missing, the user is notified prompting correction:

![checkout-invalid](readme-images/project-walkthrough/checkout-invalid-form-fields.png)

On a valid form and payment submission, the stripe intent is created, updated, succeed and charged. The order is created and the user is able to see the confirmation which includes the order summary with a auto generated order number:


![order-confirmed](readme-images/project-walkthrough/order-confirmed.png)

Once the order is created, a order confirmation is also sent out to the user via email:

![order-confirmation-arrival](readme-images/project-walkthrough/order-confirmation-arrival.png)

![order-confirmation-email](readme-images/project-walkthrough/order-confirmation-email.png)

The payment transaction can be verified from the stripe dashboard:

![ stripe-receipt](readme-images/project-walkthrough/stripe-receipt.png)

To demonstrate that the order has been created successfully within the database, the admin panel has been inspected and under "Pizza orders" the order just created can be seen in detail:

![order-created-admin-inspection](readme-images/project-walkthrough/order-created-admin.png)

**Please note**: the login to admin panel is solely to demonstrate that the order has been created succesfully with the correct order information from the cart and checkout. There is no tasks required in the admin panel for this functionality to work.

[Back to Contents.](#table-of-contents)

## Login and Registration

### Register: standard user

In addition to placing orders anonymously, the site provides the functionality for users to be able to see all the orders that they have placed.

In order to access this functionality, the user would need to register and login. This requirement is manadatory so that the orders can be attached to the logged in user only. 

To register, the user would simply click on the person icon on the menu bar and select "register" from the drop down which would navigate to the following page:

![register](readme-images/project-walkthrough/register.png)

The registration process is simple; an username, optional email address and password created in line with the password guidance provided. Once the account has been created, the user is logged and welcomed:

![user-welcome](readme-images/project-walkthrough/user-welcome.png)

From here the process to view the menu, see product details, add/remove items to the cart, check and pay is identical to that of a non logged in user which has been covered earlier in this section.

On successful completion of an order, it can now be seen by navigating to the "my orders" section from the menu:

![my-orders-link](readme-images/project-walkthrough/my-orders.png)

This page provides a count and list of all the orders that the logged in user has created, which are organised to show the latest at the top:

![my-order-page](readme-images/project-walkthrough/my-order-page.png)

Once the user has completed their activity, they are able to simply log out using the option from the menu. On doing so, the account is now secure, and any order/account information is no longer accessible.

[Back to Contents.](#table-of-contents)

## Management

### Login: manager

As mentioned at the beginning of this project walk through, the *manager* account has been elevated to a "is staff" status allowing  them to manage the site using CRUD completely on the front end.

The log in procedure is the same as a standard user, and once logged in there a few noticable difference in the options available and the UX:

![manager-login-view](readme-images/project-walkthrough/manager-login-view.png)

On the menu bar there is additional "toolbox" icon that is now available. The options within include:

![manager-menu](readme-images/project-walkthrough/manager-menu.png)


The main menu page now includes the options to delete and update a product along with the status of the all the products:

![manager-menu-2](readme-images/project-walkthrough/manager-menu-2.png)

The *manager* has full overview of all the items that exist on the menu. These include items that are active - visible on the live site and items that are in the database but not active.

### Update 

To update an item, "update" is selected which presents a form with all the current information for the item pre-populated:

![update-product](readme-images/project-walkthrough/update-product.png)

From this form, any of the details can be updated as required. The mandatory fields are marked up with an asterix.

On clicking submit, the form is validated and the updates made reflecting instantly on the live menu with a notification given in the top right corner indicating the sucessful update:

![successful-update](readme-images/project-walkthrough//update-success.png)

### Delete

The action to delete is carried out in the same manner; by selecting "delete" on the selected product which prompts a confirmation:

![delete-confirm](readme-images/project-walkthrough/delete-confirm.png)

As seen from the confirmation image above, the manager is provided with some vital information and given an alternative to permanently deleting.

Should the delete be confirmed, the item is deleted from the menu and database with a notification given:

![delete-notification](readme-images/project-walkthrough/delete-notification.png)

### Add item

From the "tool box" icon now available, selecting either the option to either add a new pizza/deal or extra presents fresh item form:

![new-item](readme-images/project-walkthrough/add-new-item.png)

Similiar to the update form, all the manditory fields are highlighted. The name for each product is required to be unique so that there is no duplication of items across the menu. 

Should the name already be in use on another item, the site informs the manager accordingly:

![duplicate-item-name](readme-images/project-walkthrough/duplicate-item-name.png)

Once rectified, along with the remainder valid form, the item is added onto the menu. Depending on the active state, the item can be seen on the live menu. In line with the rest of the notifications, a message is displayed informing of the succesfull addition.

### Order Dashboard

A key feature for the *manager* is to be able to see a live dashboard of all the current orders along with their state. This can be seen by navigating to the "Order Dashboard" from the "tool box" icon:

![order-dashboard](readme-images/project-walkthrough/order-dashboard.png)


The page presents the orders in an easy to ready way - especially in a very busy kitchen! They are categorised into "ordered", "preparing" and "ready" respectively. Each section heading provides a count of the items within that section.

Updating the order status is quick and easy; simply select the order to update by clicking "update" which prompts the following:

![update-order-status](readme-images/project-walkthrough/update-order-status.png)

Selecting the relevant status and clicking submit updates the status for that order and the order is placed in the respective section. The count for the section it moved from/to are also updated to reflect the change.

Once an order is ready and been collected, it is recommended to change the status to "Completed" so that it can be taken off the dashboard.

Any users that have created orders whilst logged in, will be able to see the updated status within their orders section allowing for them to plan their trip down to D's.

[Back to Contents.](#table-of-contents)

## About Us

Last but not least, navigating to the about us page the user is able to casually read up on the D's business ethos and values promoting how they stand out from the their competitors.

Should the user wish to stay up to date on any latest offers or deals, there is the option to subscribe towards the bottom of the page which has been provided courtesy of mail chimp. On subscribing, the user is notified:


![sucessful-subscribe](readme-images/project-walkthrough/sucessful-subscribe.png)

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

To summarise, the following sections are covered:





### Manual Testing

The following manual testing

The following manual testing has been carried out to confirm if the site's performance and functionality matched the expected output. It has tested both JavaScript and Python functionality.

### Automated Testing - scripts

There is currently no automated tested conducted in this project.

### User Story testing









  
