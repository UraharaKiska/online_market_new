from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from .services import *


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="photo_user/%Y/%m/%d", null=True, verbose_name='photo', blank=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=16, null=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            self.photo = make_thumbnail(self.photo, self.username)
            super().save(*args, **kwargs)
   