# E-Commerce API Service

This project is a Django-based e-commerce API service that provides the following features:
- User signup and login using JWT auth
- Add products to a cart
- Remove products from a cart
- View and search for products
- Checkout using Stripe

## Installation

First, clone the repository from GitHub:
  
`git clone https://github.com/samjove/e-commerce-api.git`
   
`cd e-commerce-api`

Set up a virtual environment and run

`pip install -r requirements.txt`


You will also have to set up a .env file and include the following values, with the DB values corresponding to your postgres setup:

`DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, STRIPE_TEST_SECRET_KEY, STRIPE_TEST_PUB_KEY, DOMAIN`

Run the migrations to set up the database:

`python manage.py migrate`

Start the server:

`python manage.py runserver`

To run tests:

`python manage.py test`

## API Endpoints

### Sign up:

POST `/users/register/` with the username, email, and password as the body.

### Login:

POST `/api/token/` with the username and password to obtain an access token.

Include the access token as an authorization header Bearer token for each requst.

### Products:

GET `/products/` to retrieve the product list.

GET `/products?search=<search_term>` to match product titles, categories and description with a term.

POST `/products` with product title, description, category, price and stock quantity as the body.

### Cart:

POST `/cart/add/` with a product id and quantity to add it to the cart.

GET `/cart/` to retrieve the cart.

DELETE `/cart/remove/` with a product id to remove it from the cart.

POST `/cart/checkout/` to initiate a checkout and receive a Stripe checkout session id.

## Stripe Integration

Set up a Stripe account by logging into [Stripe](https://dashboard.stripe.com/) and create a new project.

You will then be able to obtain a Stripe test secret key to add to your .env file.


See project requirements [here](https://roadmap.sh/projects/ecommerce-api).