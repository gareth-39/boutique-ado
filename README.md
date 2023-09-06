# Retro Football kits - Project Portfolio 5 - E-Commerce
![screenshot](/testing/testing/i%20am%20responsive.png)

Retro football kits is an e-commerce store were users can find retro kits, jackets and boots from there favourite teams all in one place.

Site users can create an account log in, browse and purchase items using our secure checkout area. They can also contact us by email for any enquiry they might have.

Here is a link to the live site hosted on heroku
[live website](https://retro-football-kits-17e2f93d4b27.herokuapp.com/)

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
- As a site admin i want to be able to view tickets and delete when finished.

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
- Here are some images to showcase my webite.<br><br>
![screenshot](/testing/testing/homepage.png)<br><br>
![screenshot](/testing/testing/all%20products%20page.png)<br><br>
![screenshot](/testing/testing/checkout%20page.png)<br><br>
![screenshot](/testing/testing/edit%20and%20delete.png)<br><br>
![screenshot](/testing/testing/admin%20panel.png)<br><br>
![screenshot](/testing/testing/footer.png)<br><br>
![screenshot](/testing/testing/shopping%20bag.png)<br><br>
![screenshot](/testing/testing/national%20jerseys.png)<br><br>
![screenshot](/testing/testing/national%20jackets.png)<br><br>
![screenshot](/testing/testing/prem%20jackets.png)<br><br>
![screenshot](/testing/testing/prem%20jerseys.png)<br><br>
![screenshot](/testing/testing/special%20items.png)<br><br>
![screenshot](/testing/testing/product%20management.png)<br><br>
![screenshot](/testing/testing/ticket%20page.png)<br><br>
![screenshot](/testing/testing/open%20ticket.png)<br><br>
![screenshot](/testing/testing/ticket%20closed.png)<br><br>
![screenshot](/testing/testing/successful%20checkout.png)

# Facebook
- As part of the project we needed a facebook page to match ourproject here is mine.
![screenshot](/testing/testing/facebook%20page%201.png)<br><br>
![screenshot](/testing/testing/facebook%20page%202.png)

# Custom Code
- Also as part of our project we must add three custom codes i choose a privacy, contact and Faq page.
![screenshot](/testing/testing/privacy%20page.png)<br><br>
![screenshot](/testing/testing/contact%20page.png)<br><br>
![screenshot](/testing/testing/faq%20page.png)<br><br>

# Wireframes
![screenshot](/testing/testing/home%20wire.png)<br><br>
![screenshot](/testing/testing/products%20wire.png)

# Testing
-  ## Lighthouse Testing
![screenshot](/testing/testing/lighthouse%20homepage.png)<br><br>
![screenshot](/testing/testing/lighthouse%20all%20products.png)<br><br>
![screenshot](/testing/testing/checkout%20lighthouse.png)<br><br>
![screenshot](/testing/testing/lighthouse%20privacy%20page.png)<br><br>
![screenshot](/testing/testing/lighthouse%20faq.png)<br><br>
![screenshot](/testing/testing/lghthouse%20contact.png)<br><br>

# Testing
- ## Code Validator Html

- As my code source contains (Jinja syntax `{% url 'privacy' %}`) I tested my code on the actual site, I right clicked on the homepage clicked view source code copied the code and put it into the validator this is the out come.
![screenshot](/testing/testing/html%20view%20source.png)

## Css
### Base Css
![screenshot](/testing/testing/base%20css.png)
<br><br>

### Checkout Css
![screenshot](/testing/testing/checkout%20css.png)
<br><br>

### Profile Css
![screenshot](/testing/testing/profile%20css.png)

## Javascript JShint Validator
### Countryfields
![screenshot](/testing/testing/countryfield%20profile%20js.png)
<br><br>

### Stripe
![screenshot](/testing/testing/stripe%20js.png)

## Python CI Python Linter
![screenshot](/testing/testing/bag%20contexts.py.png)<br><br>
![screenshot](/testing/testing/bag%20models.py.png)<br><br>
![screenshot](/testing/testing/bag%20views.py.png)<br><br>
![screenshot](/testing/testing/checkout%20admin.py.png)<br><br>
![screenshot](/testing/testing/checkout%20apps.py.png)<br><br>
![screenshot](/testing/testing/checkout%20forms.py.png)<br><br>
![screenshot](/testing/testing/checkout%20models.py.png)<br><br>
![screenshot](/testing/testing/checkout%20signals.py.png)<br><br>
![screenshot](/testing/testing/contact%20admin.py.png)<br><br>
![screenshot](/testing//testing/contact%20forms.py.png)<br><br>
![screenshot](/testing//testing/contact%20models.py.png)<br><br>
![screenshot](/testing/testing/contact%20views.py.png)<br><br>
![screenshot](/testing/testing/home%20views.py.png)<br><br>
![screenshot](/testing/testing/privacy%20models.py.png)<br><br>
![screenshot](/testing/testing/privacy%20views.py.png)<br><br>
![screenshot](/testing/testing/product%20admin.py.png)<br><br>
![screenshot](/testing/testing/product%20forms.py.png)<br><br>
![screenshot](/testing/testing/product%20models.py.png)<br><br>
![screenshot](/testing/testing/product%20views.py.png)<br><br>
![screenshot](/testing/testing/profile%20forms.py.png)<br><br>
![screenshot](/testing/testing/profile%20models.py.png)<br><br>
![screenshot](/testing/testing/profile%20views.py.png)<br><br>
![screenshot](/testing/testing/retro%20settings.py.png)<br><br>
![screenshot](/testing/testing/retro%20views.py.png)<br><br>
![screenshot](/testing/testing/webhook.py.png)<br><br>
![screenshot](/testing/testing/wh%20handler.py.png)<br><br>

# Manual Website testing
![screenshot](/testing/testing/successful%20checkout.png)<br><br>
![screenshot](/testing/testing/sign%20in.png)<br><br>
![screenshot](/testing/testing/sign%20in%20success.png)
<br><br>

# User Story Testing
![screenshot](/testing/user%20story/user%20stories/to%20do.png)<br><br>
![screenshot](/testing/user%20story/user%20stories/closed%20stories%201.png)<br><br>
![screenshot](/testing/user%20story/user%20stories/closed%20stories%202.png)<br><br>
![screenshot](/testing/user%20story/user%20stories/closed%20stories%203.png)<br>
![screenshot](/testing/user%20story/user%20stories/finished%20user%20stories.png)
<br><br>

# I Am Responsive
![screenshot](/testing/testing/i%20am%20responsive.png)

# Future Features

## Stock Control
- In future i would like to implement a system were the user can see what quantity of stock each product has.
-  I would also like to add a 24hour chat bot to help filter enquiries.

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

* https://mdbootstrap.com/ for my footer including social media buttons and my contact page

* https://www.privacypolicygenerator.info/ for my privay page template

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