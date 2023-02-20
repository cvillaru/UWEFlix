from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.password_validation import validate_password

class Address(models.Model): 
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.street_number + ' ' + self.street


class ContactDetails(models.Model):
    mobile_number = models.CharField(max_length=50)
    landline_number = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email


class Club(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    contact_details = models.ForeignKey(ContactDetails, on_delete=models.CASCADE, null=True)
    club_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.club_name
