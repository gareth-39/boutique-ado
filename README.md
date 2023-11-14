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
<br><br>

# Facebook
- As part of the project we needed a facebook page to match our project here is mine.
![screenshot](/testing/testing/facebook%20page%201.png)<br><br>
![screenshot](/testing/testing/facebook%20page%202.png)

# Custom Code
- Also as part of our project we must add three custom codes i choose a privacy, contact and Faq page. As my fail grade on the assessment said there was not enough custom code i have now added two extra custom logics.
![screenshot](/testing/testing/privacy%20page.png)<br><br>
![screenshot](/testing/testing/contact%20page.png)<br><br>
![screenshot](/testing/testing/faq%20page.png)<br><br>
![screenshot](/testing/testing/customer%20review%20form.png)<br><br>
![screenshot](/testing/testing/customer%20screenshot%20option.png)<br><br>

# Wireframes
![screenshot](/testing/testing/home%20wire.png)<br><br>
![screenshot](/testing/testing/products%20wire.png)

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

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

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com/), a platform as a service that enables developers to build, run and operate applications entirely in the cloud.

- Select **new** in the top-right hand corner in your heroku dashboard and select **create new app** from the dropdown menu.
- Your app name must be unique, then choose the region closest to you, then slect **create app**.
- From the new app settings, click **reveal config vars** ans set your enviroment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | Insert your own API key here. |
| `DATABASE_URL` | insert your own ElephantSQL database url here. |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary and can be removed on your final deployment*) |
| `SECRET_KEY` | This can be any random secret key. |
| `AWS_SECRET_ACCESS_KEY` | Insert your own API key here. | |
| `EMAIL_HOST_PASS` | Insert your own API key here. | |
| `EMAIL_HOST_USER` | Insert your own email here. | |
| `STRIPE_PUBLIC_KEY` | Insert your own API key here. | | | |
| `STRIPE_SECRET_KEY` | Insert your own API key here. | | | |
| `STRIPE_WH_SECRET` | Insert your own API key here. | | | |
| `USE_AWS` | Set to true. | | | |


Heroku needs two additional files in order to deploy properly.
- requirements.txt file.
- Procfile.

You can install this projects ** requirements** using:
- `pip3 install -r requirements.txt`

If you have your own package that have been installed , then the requirements file needs updating using:
- `pip3 freeze --local > requirements.txt`

The **profile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Profile`
- Make sure to replace 'app_name' with the name of your **own** app name.

For Heroku deployment, follow these steps to deploy your site:

- **Automatic** select 'enable automatic deployment'.
- **Manual deployment** can be done by:
    - By typing `heroku login -i` in the terminal.
    - Set the remote for heroku: `heroku git:remote -a app_name` replace 'app_name' with your own app name.

### Cloning 

You can clone this repository by follwoing these steps:

- Go to the [GitHub repository](https://github.com/AdamRalph123/Car-talk-blog).
- Locate the code button above the list of files and click it.
- Select if you prefer to clone using HTTPS, SSH or GitHub CLI and click copy button to copy the URL to your clipboard.
- Open Git bash or Terminal.
- Chanhe the current working directory to the one you the clonned directory.
- In your IDE terminal, type the following command to clone the repository: `git clone https://github.com/AdamRalph123/Car-talk-blog`.
- Press enter to create your clone.

### Forking

By forking this GitHub repository, you make a copy of the original repository on your GitHub account to view or makw chnages to it without affecting the ownders repository.

Follow these steps to fork this repository:

- Login into GitHub and locate [GitHub repository](https://github.com/AdamRalph123/Car-talk-blog).
- At the top of the repository Just above the **settings** button on the menu, locate the **fork** button.
- Once clicked, you should now have a copy of the original repository in your own GitHub account.


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