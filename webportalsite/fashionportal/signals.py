from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from registration.users import UserModel

from .models import UserProfile

@receiver(post_save, sender = UserModel)
def create_profile_handler(sender, instance, created, **kwargs):
	if not created:
		return

		profile = UserProfile(user=instance)
		profile.save()