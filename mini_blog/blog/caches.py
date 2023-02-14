from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache

# we are using cache + signals here
@receiver(user_logged_in, sender=User)
def login_count(sender, request, user, **kwargs):
    ct = cache.get('count', 0, version=user.pk)
    new_count = ct + 1
    cache.set('count', new_count, 60*60*24, version=user.pk)