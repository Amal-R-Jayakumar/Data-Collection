import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.core.validators import RegexValidator
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=150)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=300)
    course = models.CharField(max_length=300)
    year_joined = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    dob = models.DateField()
    gender = models.CharField(max_length=50)
    address = models.TextField()
    photo = models.ImageField(
        default='images/default.png', upload_to='images/profile_pics')

    # phone_regex = RegexValidator(
    #     regex=r'^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$', message="Phone number entered incorrectly.")
    # phone_number = models.CharField(
    #     validators=[phone_regex], max_length=17, blank=True)
    
    
