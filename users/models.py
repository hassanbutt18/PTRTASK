from django.db import models
from django.contrib.auth.models import AbstractUser
from users.manager import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, auto_now=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
            # self.user_name = self.email.lower()
        super(User, self).save(*args, **kwargs)
