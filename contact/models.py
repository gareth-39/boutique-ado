from django.db import models
from django.utils import timezone
from django import forms

class Ticket(models.Model):
    """
    Created when a user submits a form on the contact page
    """
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    sent_at = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)
    image1 = forms.Field(label='sample photo', widget = forms.FileInput, required = True )
