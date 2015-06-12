from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from fashionportal.models import Gallery, Thumbnail, LargePictures, News, Event, Address, UserProfile, Job, Shop

class JobAdmin(admin.ModelAdmin):
	model = Job
	exclude = ('document',)

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False

class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, )

class ThumbnailInline(admin.TabularInline):
	model = Thumbnail

class LargePicturesInline(admin.TabularInline):
	model = LargePictures

class GalleryAdmin(admin.ModelAdmin):
	inlines = [ThumbnailInline, LargePicturesInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Gallery, GalleryAdmin)

admin.site.register(News)

admin.site.register(Address)
admin.site.register(Event)



# Register your models here.





