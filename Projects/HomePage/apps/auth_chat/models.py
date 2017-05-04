from django.conf import settings
from django.contrib import auth
from django.db import models

# User = auth.get_user_model()

class LoggedInUser(models.Model):
    # user = models.OneToOneField(User, related_name='logged_in_user')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user')
