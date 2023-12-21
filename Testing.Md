# Testing

Return back to the [README.md](README.md) file.

## Code validation

### HTML

I have used the recommened [HTML w3c validator](https://validator.w3.org/) to test and validate all of my html files.

All of my validations have now been fixed and are showing no errors or warnings

As my project uses Jinja syntax such as, `{% for loops %}` and `{% url 'home' %}` if will not validate properly if I copy and paste my code straight from my workspace.

In order to properly validate my HTML pages with Jinja syntax for authenticated pages, I followed these steps.

- Navigate to the deployed page which requires authentication.
- Right click anywhere on the page and select **View page source** or `CTRL+U`.
- This will display the compiled code without any Jinja syntax.
- Copy all the code (CTRL+A) and use the [Validate by input](https://validator.w3.org/#validate_by_input)


| Pages | Screenshots | Notes |
| --- | --- | --- |
| Home | ![screenshot](/testing/testing/new%20validations.png) | 7 errors |


### CSS
 
 I have used the recommneded [CSS Jigsaw validator](https://jigsaw.w3.org/css-validator/) to validate my css file.

| File | Screenshot | Notes |
| --- | --- | --- |
| base.css | ![screenshot](/testing/testing/base%20css.png) | Pass: no errors |
| profile.css | ![screenshot](/testing/testing/profile%20css.png) | Pass: no errors |
| cheackout.css | ![screenshot](/testing/testing/checkout%20css.png) | Pass: no errors |
<br><br>


### JavaScript

I have used [JShint validator](https://jshint.com/) to validate my javascript code that is found in my base.html file.

| File | Screenshot | Notes |
| --- | --- | --- |
| country field | ![screenshot](/testing/testing/countryfield%20profile%20js.png) | Pass: no errors |

# Stripe

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe | ![screenshot](/testing/testing/stripe%20js.png) | Pass: no errors |

# Python CI Python Linter

I have used [CI Python linter](https://pep8ci.herokuapp.com/) to validate all of my python files.

| File | Screenshot | Notes |
| --- | --- | --- |
| bag contexts.py | ![screenshot](/testing/testing/bag%20contexts.py.png) | Pass: no errors | 
| bag models.py | ![screenshot](/testing/testing/bag%20models.py.png) | Pass: no errors | 
| bag views.py | ![screenshot](/testing/testing/bag%20views.py.png) | Pass: no errors |
| bagviews.py | ![screenshot](/testing/testing/bag%20views.py.png) | Pass: no errors |
| checkout admin.py | ![screenshot](/testing/testing/checkout%20admin.py.png) | Pass: no errors | 
| checkout apps.py | ![screenshot](/testing/testing/checkout%20apps.py.png)| Pass: no errors | 
| checkout forms.py | ![screenshot](/testing/testing/checkout%20forms.py.png) | Pass: no errors | 
| checkout models.py | ![screenshot](/testing/testing/checkout%20models.py.png) | Pass: no errors | 
| checkout signals.py | ![screenshot](/testing/testing/checkout%20signals.py.png) | Pass: no errors |
| contact admin.py | ![screenshot](/testing/testing/contact%20admin.py.png) | Pass: no errors |
| contact forms.py | ![screenshot](/testing//testing/contact%20forms.py.png) | Pass: no errors |
| contact models.py | ![screenshot](/testing//testing/contact%20models.py.png) | Pass: no errors |
| contact views.py | ![screenshot](/testing/testing/contact%20views.py.png) | Pass: no errors |
| home views.py | ![screenshot](/testing/testing/home%20views.py.png) | Pass: no errors |
| privacy models.py | ![screenshot](/testing/testing/privacy%20models.py.png) | Pass: no errors | 
| privacy views.py | ![screenshot](/testing/testing/privacy%20views.py.png) | Pass: no errors |
| product admin.py | ![screenshot](/testing/testing/product%20admin.py.png) | Pass: no errors | 
| product forms.py | ![screenshot](/testing/testing/product%20forms.py.png) | Pass: no errors |
| product models.py | ![screenshot](/testing/testing/product%20models.py.png) | Pass: no errors |
| product views.py | ![screenshot](/testing/testing/product%20views.py.png) | Pass: no errors |
| profile forms.py | ![screenshot](/testing/testing/profile%20forms.py.png) | Pass: no errors |
| profile models.py | ![screenshot](/testing/testing/profile%20models.py.png)| Pass: no errors |
| profile views.py | ![screenshot](/testing/testing/profile%20views.py.png) | Pass: no errors |
| retro settings.py | ![screenshot](/testing/testing/retro%20settings.py.png) | Pass: no errors |
| retro views.py | ![screenshot](/testing/testing/retro%20views.py.png) | Pass: no errors |
| webhook.py | ![screenshot](/testing/testing/webhook.py.png) | Pass: no errors |
| w/h handler.py | ![screenshot](/testing/testing/wh%20handler.py.png) | Pass: no errors |
<br><br>

# Manual Website testing

Manual testing is used below to make sure the sites functionality is working and does not crash or cause any errors.

| Page | User action | Expected result | Pass/fail |
| --- | --- | --- | --- |
| Home page | Click on logo | Redirected to home page | Pass |
| Sign up | Click on Register navigation | Brings user to sign up page. User is asked to enter username, email address and password. Click submit, user is directed to home page. | Pass |
| Sign in | Click on Sign in navigation | Redirected to sign in page. User must enter the correct Sign in details. When entered correctly users will be directed to the home page with a message appearing to let the user know they are signed in. | Pass |
| Sign out | Click on sign out navigation | User will be redirected to a sign out comfirmation page. When user signs out they will be brought to the home page with a message appearing to let the user know they are signed out. | Pass |
| Review | Type review and submit | users will be notified that their review has been added. | Pass |
| Add item to bag | Click on an product | user will be notified that a product has been added tp their bag | Pass |
| contact form | fill out form and submit | When the user fills out a contact form the user will receive an email to say that their query has been notified. | Pass |
| subscribe button | Click on subscribe button | when a user enters their emaill address and clicks subscribe they will be notified that they have been subscribed | Pass |
| Add/remove item from bag | click add/ remove button | when the user clicks add/remove in the shopping bag that will be notified | Pass |


### User Story Testing

| File | Screenshot |
| --- | --- |
![screenshot](/testing/user%20story/user%20stories/to%20do.png)<br><br>
![screenshot](/testing/user%20story/user%20stories/closed%20stories%201.png)<br><br>
![screenshot](/testing/user%20story/user%20stories/closed%20stories%202.png)<br><br>
![screenshot](/testing/user%20story/user%20stories/closed%20stories%203.png)<br><br>
![screenshot](/testing/user%20story/user%20stories/finished%20user%20stories.png)
<br><br>

 ### MoSCow prioritization

- **Must have**: The 'MUST' level requirements are those requirements which will definitely be included to be delivered.
- **Should have**: The 'SHOULD' level requirements are those requirements which should be included if at all possible. If the project has capacity and time and it will not jeopardise any of the 'must have' requirements.
- **Could have**: The 'COULD' level requirements are the requirements which could be included if it doesnt have any impact on any of the 'should' or 'must' requirements.
- **Wont have**: The 'WONT' level requirements tend to be the requirements which will not be  included or implemented this time but are requirements that would be favoured for a future delivery or implementation.

### Am I Responsive
Checked on the i am responsive webite. [Am I Responsive](https://ui.dev/amiresponsive)

| File | Screenshot | Notes |
| --- | --- | --- |
| responsive | ![screenshot](/testing/testing/changed%20responsive.png) | all responsive |

 ### Lighthouse Testing

| File | Screenshot | Notes |
| --- | --- | --- |
| homepage | ![screenshot](/testing/testing/lighthouse%20homepage.png) 
| products | ![screenshot](/testing/testing/lighthouse%20all%20products.png)
| checkout | ![screenshot](/testing/testing/checkout%20lighthouse.png)
| privacy | ![screenshot](/testing/testing/lighthouse%20privacy%20page.png)
| faq | ![screenshot](/testing/testing/lighthouse%20faq.png)
| contact | ![screenshot](/testing/testing/lghthouse%20contact.png)