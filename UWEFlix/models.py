from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password

class Address(models.Model): 
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.postcode

class ContactDetails(models.Model):
    mobile_number = models.CharField(max_length=11)
    landline_number = models.CharField(max_length=11)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email

class Club(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    contact_details = models.ForeignKey(ContactDetails, on_delete=models.CASCADE, null=True)
    club_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.club_name
    
class ClubRepresentative(models.Model):
    representClub = models.OneToOneField(Club,on_delete=models.PROTECT,null=True)
    user = models.OneToOneField(User,on_delete=models.PROTECT,null=True)
    clubNumber = models.CharField(max_length=6,default='000000')
    
    def __str__(self) -> str:
        return self.clubNumber
