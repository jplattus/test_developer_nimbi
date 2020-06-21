from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Navigation(models.Model):
    user = models.CharField(_('user'), max_length=20)
    session = models.CharField(_('session'), max_length=20)
    path = models.CharField(_('path'), max_length=200)
    access_time = models.DateTimeField(auto_now_add=True)
