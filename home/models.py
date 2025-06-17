# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Harsha Pg For Gents(models.Model):

    #__Harsha Pg For Gents_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    rent = models.IntegerField(null=True, blank=True)
    date of joining = models.DateTimeField(blank=True, null=True, default=timezone.now)
    date of vacate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    advance = models.IntegerField(null=True, blank=True)

    #__Harsha Pg For Gents_FIELDS__END

    class Meta:
        verbose_name        = _("Harsha Pg For Gents")
        verbose_name_plural = _("Harsha Pg For Gents")



#__MODELS__END
