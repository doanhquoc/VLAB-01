from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class WorkInfor(models.Model):
    WorkName_text = models.CharField(max_length=200, default =None)
    Company_text = models.CharField(max_length=200, default =None)
    LevelChoice = (
        ('intership', 'intership'),
        ('fresher', 'fresher'),
        ('senior', 'senior'),
        ('junior', 'junior'),
    )
    level = models.CharField(max_length=200, choices=LevelChoice, default='intership')
    Description_text = models.CharField(max_length=500, default=None)
    LevelTime = (
        ('3 hours', '3 hours'),
        ('12 hours', '12 hours'),
        ('2 days', '2 days'),
    )
    LongTime = models.CharField(max_length=200, choices=LevelTime, default='3 hours')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list
    photo = models.ImageField(upload_to='WorkImages', default=None, blank=True)
    money = models.DecimalField(max_digits=12, decimal_places=2, default=None)
