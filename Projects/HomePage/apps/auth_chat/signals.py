from django.conf import settings
from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import LoggedInUser


# @receiver(user_logged_in, sender=settings.AUTH_USER_MODEL)
@receiver(user_logged_in)
def on_user_login(sender, **kwargs):
	print('log in')
	LoggedInUser.objects.get_or_create(user=kwargs.get('user'))


# @receiver(user_logged_out, sender=settings.AUTH_USER_MODEL)
@receiver(user_logged_out)
def on_user_logout(sender, **kwargs):
	print('log out')
	LoggedInUser.objects.filter(user=kwargs.get('user')).delete()

# user_logged_in.connect(on_user_login)
# user_logged_in.connect(on_user_logout)
