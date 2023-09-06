# Retro Football kits - Project Portfolio 5 - E-Commerce
![screenshot](/testing/testing/i%20am%20responsive.png)

Retro football kits is an e-commerce store were users can find retro kits, jackets and boots from there favourite teams all in one place.

Site users can create an account log in, browse and purchase items using our secure checkout area. They can also contact us by email for any enquiry they might have.

Here is a link to the live site hosted on heroku
[live website]

Here is a link to my gitpod repository https://github.com/gareth-39/Retro-football-kits

# Table of Contents:
* User Stories
* Libraries and technologies
* Expectations
* Functionality
* UX/UI
* Main site image
* Features
* Facebook
* Custom Code
* Wireframes
* Testing
* Future features
* Bugs and errors
* Deployment
* Credits
* Icons
* Fonts
* Programs used
* My thanks<br><br>

# User Stories
### Site Admin
- As a site admin i wanted to be able to add and delete products when i needed.
- As a site admin i also wanted to be able to edit items when i have too.
- As a site admin i to navigate to the admin panel when i need too.

### Site User
- As a first time user i want to be able to register for the site and have the option to save my details so the site remembers me the next time i login.
- As a site user i want to be able to search for products quickly.
- As a site user i want to see my shopping bag and its contents clearly.
- As a site user i want access to the privacy, contact, faq and social media sites with one click.
- As a site user i want to see how much i am spending as i add products to my basket.
- As a site user i want to be able to add and remove produts from my bag.
- As a site user i want to see the price of all the products.
- As a site user i want to subscribe to the newsletter.
- As a site user i want the site to save my billing and shipping details for future purchases.
- As a site user i want to recieve an email to confirm my order.


# Libraries and technologies used:
- Django
- Crispy forms
- Cloudinary
- Bootstrap
- Python
- Elephant Sql
- Heroku
- Mailchimp
- Stripe

# Expectations 
- Corresponds to all screen sizes and devices.
- Accessible and user friendly site.
- User friendly and clear navigation methods.
- Every part of my site is functional as intended.
- Each  button is functional and corresponded accordingly when pressed.
- Responsive on all devices irrespective of users choice.
- All functions worked as they should and in a clear and concise manner.

# Functionality
* All buttons and links have been hovered over and clicked on to ensure accessibility.
* All pages load correctly across all device screen sizes (Please see testing section).
* Functional buttons worked as intended and on different device screen sizes.

# Ux/Ui
- My site uses manily black  `rgb(255, 255, 255) ` and white `:rgb(16, 0, 0)` colours as i think it makes the site stand out to the user and is very clear.
- Other colour have also been used for button that are clicked or hovered over here is a list.
* `rgb(0, 123, 255)`  
* `rgb(40, 167, 69)` 
* `rgb(108, 117, 125)`  
* `rgb(220, 53, 69)` 
* `rgb(255, 193, 7)`
* `rgb(23, 162, 184)` 
* `rgb(247, 249, 250)`

# Main site image
- Here is the main site image for my website i have used this image as i really like it but i have moved the faces on the image up on the deployed site as i was not to sure about the copyright infrigement.
![Alt text](/media/image-5%20(1).webp)

# Features
- Here is a list of images to showcase my website.
![screenshot](/testing/testing/homepage.png)
![screenshot](/testing/testing/all%20products%20page.png)
![screenshot](/testing/testing/checkout%20page.png)
![screenshot](/testing/testing/edit%20and%20delete.png)
![screenshot](/testing/testing/admin%20panel.png)
![screenshot](/testing/testing/footer.png)
![screenshot](/testing/testing/shopping%20bag.png)
![screenshot](/testing/testing/national%20jerseys.png)
![screenshot](/testing/testing/national%20jackets.png)
![screenshot](/testing/testing/prem%20jackets.png)
![screenshot](/testing/testing/prem%20jerseys.png)
![screenshot](/testing/testing/special%20items.png)
![screenshot](/testing/testing/product%20management.png)

# Facebook
- As part of the project we needed a facebook page to match ourproject here is mine.
![screenshot](/testing/testing/facebook%20page%201.png)
![screenshot](/testing/testing/facebook%20page%202.png)

# Custom Code
- Also as part of our project we must add three custom codes i choose a privacy, contact and Faq page.
![screenshot](/testing/testing/privacy%20page.png)
![screenshot](/testing/testing/contact%20page.png)
![screenshot](/testing/testing/faq%20page.png)

# Wireframes
![screenshot](/testing/testing/home%20wire.png)
![screenshot](/testing/testing/products%20wire.png)

# Testing
-  ## Lighthouse Testing
![screenshot](/testing/testing/lighthouse%20homepage.png)
![screenshot](/testing/testing/lighthouse%20all%20products.png)
![screenshot](/testing/testing/checkout%20lighthouse.png)
![screenshot](/testing/testing/lighthouse%20privacy%20page.png)
![screenshot](/testing/testing/lighthouse%20faq.png)
![screenshot](/testing/testing/lghthouse%20contact.png)

# Testing
- ## Code Validator Html

- As my code source contains (Jinja syntax `{% url 'privacy' %}`) I tested my code on the actual site, I right clicked on the homepage clicked view source code copied the code and put it into the validator this is the out come.
![screenshot](/testing/testing/html%20view%20source.png)

## Css
### Base Css
![screenshot](/testing/testing/base%20css.png)
### Checkout Css
![screenshot](/testing/testing/checkout%20css.png)
### Profile Css
![screenshot](/testing/testing/profile%20css.png)

## Javascript JShint Validator
### Countryfields
![screenshot](/testing/testing/countryfield%20profile%20js.png)
### Stripe
![screenshot](/testing/testing/stripe%20js.png)

## Python CI Python Linter
![screenshot](/testing/testing/bag%20contexts.py.png)
![screenshot](/testing/testing/bag%20models.py.png)
![screenshot](/testing/testing/bag%20views.py.png)
![screenshot](/testing/testing/checkout%20admin.py.png)
![screenshot](/testing/testing/checkout%20apps.py.png)
![screenshot](/testing/testing/checkout%20forms.py.png)
![screenshot](/testing/testing/checkout%20models.py.png)
![screenshot](/testing/testing/checkout%20signals.py.png)
![screenshot](/testing/testing/contact%20admin.py.png)
![screenshot](/testing//testing/contact%20forms.py.png)
![screenshot](/testing//testing/contact%20models.py.png)
![screenshot](/testing/testing/contact%20views.py.png)
![screenshot](/testing/testing/home%20views.py.png)
![screenshot](/testing/testing/privacy%20models.py.png)
![screenshot](/testing/testing/privacy%20views.py.png)
![screenshot](/testing/testing/product%20admin.py.png)
![screenshot](/testing/testing/product%20forms.py.png)
![screenshot](/testing/testing/product%20models.py.png)
![screenshot](/testing/testing/product%20views.py.png)
![screenshot](/testing/testing/profile%20forms.py.png)
![screenshot](/testing/testing/profile%20models.py.png)
![screenshot](/testing/testing/profile%20views.py.png)
![screenshot](/testing/testing/retro%20settings.py.png)
![screenshot](/testing/testing/retro%20views.py.png)
![screenshot](/testing/testing/webhook.py.png)
![screenshot](/testing/testing/wh%20handler.py.png)

# Manual Website testing
![screenshot](/testing/testing/successful%20checkout.png)
![screenshot](/testing/testing/sign%20in.png)
![screenshot](/testing/testing/sign%20in%20success.png)

# User Story Testing
![screenshot](/testing/user%20story/user%20stories/to%20do.png)
![screenshot](/testing/user%20story/user%20stories/closed%20stories%201.png)
![screenshot](/testing/user%20story/user%20stories/closed%20stories%202.png)
![screenshot](/testing/user%20story/user%20stories/closed%20stories%203.png)
![screenshot](/testing/user%20story/user%20stories/finished%20user%20stories.png)

# I Am Responsive
![screenshot](/testing/testing/i%20am%20responsive.png)

# Future Features

## Stock Control
- In future i would like to implement a system were the user can see what quantity of stock each product has.

# Bugs and errors:
I had so many bugs and errors on this project, here is a list of them and the solutions i encorperated.

- Error 404 page not found = `(Solution)` It was I had not linked my paths properly in my settings.py

- CSS not working on Heroku = `(Solution)` I had not changed debug to false before deployment

- Server 500 = `(Solution)` there was a problem  with the superuser deleted that user and replaced it with a new one.

- html pages not found = `(Solution)` This was a big one as it made my whole code error i changed a file name from one name to another and i didnt realise every where on the code i needed to change the name in each url file.

- Images not loading = `(Solution)` The site i was using didnt allow user to use there images.

- Build fail on heroku = `(Solution)` When I deployed through heroku the build failed not sure why just disconnected the app and re-deployed and it worked.

- Indentation errors = `(Solution)` Simple spelling mistakes that were easily fixed.

#  Deployment
* This project was deployment using Code institute's mock terminal on Heroku.

* * Sign up for heroku.
* * Create a Heroku app.
* * Add a confrig var (key) PORT (value) 8000.
* * CLOUDINARY_URL
* * DATABASE_URL
* * HEROKU_POSTGRESQL_GREEN_URL
* * SECRET_KEY
* * Link the Heroku app to my repository.
* * Build the repository.
* * Click on deploy.
* * New page opens with working app.


# Credits:

* https://www.vintagefootballshirts.com/ for the use of there images and pricing

* https://www.vintagefootballshirts.com/ aslo for the template for the Faq page

* https://www.sportbible.com/football/news-adidas-and-pharrell-williams-release-stunning-humanrace-retro-kits-20201023 For my main page image

* https://mdbootstrap.com/ for my footer including social media boes 

* Bootstrap https://getbootstrap.com/

* Code Institute https://codeinstitute.net/ie/

* Slack https://app.slack.com/

* Google http://google.com/

* Student care https://learn.codeinstitute.net/ci_support/diplomainsoftwaredevelopmentecomm/studentcare
without them i would have given up.

#

# Icons:

* Font awesome https://fontawesome.com/

#

# Fonts:

* Google fonts https://fonts.google.com/

#

# Programs used:
HTML
54.7%
 
Python
36.6%
 
CSS
4.0%
 
Dockerfile
2.4%
 
JavaScript
2.3%

# My thanks:

* Thanks to my mentor Jubril Akolade for his endless patience and answering my plethora of questions.

* Thanks to Google (https://www.google.com/) for helping me debug and troubleshoot any issue I had.

* Thanks to Code Institute https://codeinstitute.net/ie/ once again for creating the template for this blog.


* Thanks to my Slack group (https://app.slack.com/) who are so helpful and assisting me every step of the way.

# #

## FINALLY THANK YOU TO THE ASSESSMENT TEAM FOR ALL OF THE POSITIVE FEED BACK USE HAVE GIVEN ME IN ALL MY PROJECTS TO DATE.




















