from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm

from django.views.generic import UpdateView

from fashionportal.models import UserProfile, PostEntry, occupations




class EditProfileView(UpdateView):
	model = UserProfile
	fields = ['occupation','date_of_birth', 'brand_name', 'phone', 'location', 'profile_image']
	template_name = 'fashionportal/edit-profile.html'
	success_url = 'fashionportal:profile'
	slug_field = 'user__username'
	slug_url_kwarg = 'username'

	def get_success_url(self):
		return reverse(self.success_url, args=(self.request.user.username,) )

