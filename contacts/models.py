from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Person(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=11)
    email = models.EmailField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.last_name

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
#    website = models.URLField(blank=True)
#    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
