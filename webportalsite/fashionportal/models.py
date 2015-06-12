from django.db import models
from django.contrib.auth.models import User


from image_cropping import ImageRatioField

from registration.users import UserModel

from django.conf import settings
from django.core.urlresolvers import reverse






# Create your models here.

OCCUPATION_CHOICES = (
	('DESIGNER', 'Designer'),
	('MODEL', 'Model'),
	('TAILOR', 'Tailor'),
	('PHOTOGRAPHER', 'Photographer'),
)

occupations = {
'DESIGNER': 'fashionportal:designers',
'MODEL' : 'fashionportal:models',
'TAILOR' : 'fashionportal:tailors',
'PHOTOGRAPHER' : 'fashionportal:photographers'
}


class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, default=None)

	bio = models.TextField(null=True)
	phone = models.CharField(max_length=255, null=True)
	profile_image = models.ImageField('Photo', upload_to='photos', blank=True, null=True)
	occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES, default=None)
	last_login = models.DateTimeField(auto_now_add=True)
	date_of_birth = models.DateField(blank=True, null=True, default=None)
	creation_date = models.DateField(auto_now_add=True)
	cropping = ImageRatioField('profile_image', '430x360')
	brand_name = models.CharField(max_length=255, blank=True, null=True)
	location = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.user.username


from django.utils import timezone

class PostEntry(models.Model):
	posted_by = models.OneToOneField(UserProfile, primary_key=True)

	description = models.TextField()
	photo = models.ImageField('Photo', upload_to='post-photos', blank=True, default="Images", null=True)
	cropping = ImageRatioField('photo', '430x360')
	pub_date = models.DateTimeField(auto_now_add=True, default=timezone.now())


	def __str__(self):
		return self.description




class Gallery(models.Model):
	title = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.title


class Thumbnail(models.Model):
	gallery = models.ForeignKey(Gallery)
	imageTitle = models.CharField(max_length=200)
	smallImage = models.ImageField('Photo', upload_to='gallery', blank=True)
	cropping = ImageRatioField('smallImage', '1290x1080')

	def __str__(self):
		return self.imageTitle

class LargePictures(models.Model):
	gallery = models.ForeignKey(Gallery)
	imageTitle = models.CharField(max_length=200)
	largeImage = models.ImageField('Photo', upload_to='gallery', blank=True)	
	cropping = ImageRatioField('largeImage', '860x760')

class Shop(models.Model):
	name = models.CharField(max_length=255)
	website = models.URLField(max_length=255)
	image = models.ImageField(verbose_name='Photo', upload_to='shop', blank=True, null=True)
	cropping = ImageRatioField('image', '860x760')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('fashionportal:shops')

	class Meta:
		ordering = ['name']
		verbose_name_plural = []

class Job(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	document = models.FileField(verbose_name='Upload CV ', upload_to='job')


	def __str__(self):
		return self.title


	
	

class Photographer(UserProfile):
	occupation = 'PHOTOGRAPHER'

class Model(UserProfile):
	occupation = 'MODEL'

class FashionDesigner(UserProfile):
	occupation = 'DESIGNER'

class Tailor(UserProfile):
	occupation = 'TAILOR'

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)    
    post_code = models.CharField(max_length=255)

    def __str__(self):
    	return self.street


class Event(models.Model):
	title = models.CharField(max_length=255, default=None)
	description = models.TextField(default='Describe event here')
	date = models.DateTimeField(default=None)
	image = models.ImageField(upload_to='events', blank=True)
	address = models.OneToOneField(Address, default=None)
	cropping = ImageRatioField('image', '860x760')

	def __str__(self):
		return self.title

class News(models.Model):
	headline = models.CharField(max_length=255, blank=True)
	body = models.TextField(blank=True)
	image = models.ImageField(upload_to='news', blank=True)
	pub_date = models.DateTimeField(auto_now_add=True, default=None)
	cropping = ImageRatioField('image', '860x760')

	def __str__(self):
		return self.headline

	def get_absolute_url(self):
		return reverse('fashionportal:newsdetail', args=[self.id])

	class Meta:
		ordering = ['-pub_date']
		verbose_name = "News"
		verbose_name_plural = "News"





	

