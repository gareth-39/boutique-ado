# Testing

Return back to the [README.md](README.md) file.

## Code validation

### HTML

I have used the recommened [HTML w3c validator](https://validator.w3.org/) to test and validate all of my html files.

Most of my HTML files has similar issues with errors and warnings which I was not able to fix as it caused even more errors in my code.

As my project uses Jinja syntax such as, `{% for loops %}` and `{% url 'home' %}` if will not validate properly if I copy and paste my code straight from my workspace.

In order to properl validate my HTML pages with Jinja syntax for authenticated pages, I followed these steps.

- Navigate to the deployed page which requires authentication.
- Right click anywhere on the page and select **View page source** or `CTRL+U`.
- This will display the compiled code without any Jinja syntax.
- Copy all the code (CTRL+A) and use the [Validate by input](https://validator.w3.org/#validate_by_input)


| Pages | Screenshots | Notes |
| --- | --- | --- |
| Home | ![screenshot](/testing/testing/validation%20error%201.png) | 7 errors |
| Home | ![screenshot](/testing/testing/validation%20error%202.png) | 7 errors |

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

### Stripe

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe | ![screenshot](/testing/testing/stripe%20js.png) | Pass: no errors |

## Python CI Python Linter

| File | Screenshot | Notes |
| --- | --- | --- |
| bag contexts.py | ![screenshot](/testing/testing/bag%20contexts.py.png) | Pass: no errors | <br><br>
| bag models.py | ![screenshot](/testing/testing/bag%20models.py.png) | Pass: no errors | <br><br>
| bag views.py | ![screenshot](/testing/testing/bag%20views.py.png) | Pass: no errors |<br><br>
| bagviews.py | ![screenshot](/testing/testing/bag%20views.py.png) | Pass: no errors |<br><br>
| checkout admin.py | ![screenshot](/testing/testing/checkout%20admin.py.png) | Pass: no errors | <br><br>
| checkout apps.py | ![screenshot](/testing/testing/checkout%20apps.py.png)| Pass: no errors | <br><br>
| checkout forms.py | ![screenshot](/testing/testing/checkout%20forms.py.png) | Pass: no errors | <br><br>
| checkout models.py | ![screenshot](/testing/testing/checkout%20models.py.png | Pass: no errors | )<br><br>
| checkout signals.py | ![screenshot](/testing/testing/checkout%20signals.py.png) | Pass: no errors | <br><br>
| contact admin.py | ![screenshot](/testing/testing/contact%20admin.py.png) | Pass: no errors | <br><br>
| contact forms.py | ![screenshot](/testing//testing/contact%20forms.py.png) | Pass: no errors | <br><br>
| contact models.py | ![screenshot](/testing//testing/contact%20models.py.png) | Pass: no errors |<br><br>
| contact views.py | ![screenshot](/testing/testing/contact%20views.py.png) | Pass: no errors | <br><br>
| home views.py | ![screenshot](/testing/testing/home%20views.py.png) | Pass: no errors | <br><br>
| privacy models.py | ![screenshot](/testing/testing/privacy%20models.py.png | Pass: no errors | )<br><br>
| privacy views.py | ![screenshot](/testing/testing/privacy%20views.py.png) | Pass: no errors | <br><br>
| product admin.py | ![screenshot](/testing/testing/product%20admin.py.png) | Pass: no errors | <br><br>
| product forms.py | ![screenshot](/testing/testing/product%20forms.py.png) | Pass: no errors | <br><br>
| product models.py | ![screenshot](/testing/testing/product%20models.py.png) | Pass: no errors |<br><br>
| product views.py | ![screenshot](/testing/testing/product%20views.py.png) | Pass: no errors | <br><br>
| profile forms.py | ![screenshot](/testing/testing/profile%20forms.py.png) | Pass: no errors | <br><br>
| profile models.py | ![screenshot](/testing/testing/profile%20models.py.png)| Pass: no errors | <br><br>
| profile views.py | ![screenshot](/testing/testing/profile%20views.py.png) | Pass: no errors | <br><br>
| retro settings.py | ![screenshot](/testing/testing/retro%20settings.py.png) | Pass: no errors | <br><br>
| retro views.py | ![screenshot](/testing/testing/retro%20views.py.png) | Pass: no errors | <br><br>
| webhook.py | ![screenshot](/testing/testing/webhook.py.png) | Pass: no errors | <br><br>
| w/h handler.py | ![screenshot](/testing/testing/wh%20handler.py.png) | Pass: no errors | <br><br>

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

-  ### Lighthouse Testing
![screenshot](/testing/testing/lighthouse%20homepage.png)<br><br>
![screenshot](/testing/testing/lighthouse%20all%20products.png)<br><br>
![screenshot](/testing/testing/checkout%20lighthouse.png)<br><br>
![screenshot](/testing/testing/lighthouse%20privacy%20page.png)<br><br>
![screenshot](/testing/testing/lighthouse%20faq.png)<br><br>
![screenshot](/testing/testing/lghthouse%20contact.png)<br><br>