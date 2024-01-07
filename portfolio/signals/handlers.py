from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from portfolio.models import Profile

@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, **kwargs):
  if kwargs['created']:
    Profile.objects.create(user=kwargs['instance'])

# @receiver(post_save, sender=User)
# def save_profile_with_user(sender, instance, **kwargs):
#   instance.profile.save()

