from django.apps import AppConfig


class FashionPortalConfig(AppConfig):
	name = 'fashionportal'
	verbose_name = 'Fashion Portal Profiles'


	def ready(self):
		from . import signals