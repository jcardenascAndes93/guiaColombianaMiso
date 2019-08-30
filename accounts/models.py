from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField


# Profile model that extends
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = PhoneField(blank=True)
