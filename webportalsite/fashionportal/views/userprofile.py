from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth.models import User



from django.views.generic.base import TemplateView
from django.forms import ModelForm

from fashionportal.models import PostEntry, UserProfile
from blog.models import BlogEntry


def userprofile_page(request, username):
	
	member = User.objects.get(username=username)
	context = { 'member': member }
	return render(request, 'fashionportal/userprofile.html', context)


# class ProfilePageView(TemplateView):
# 	template_name = 'fashionportal/userprofile.html'

# 	def get_context_data(self,  **kwargs):
# 		context = super(ProfilePageView, self).get_context_data(**kwargs)
# 		context['blogPosts'] = BlogEntry.objects.all()
# 		return context





# def userprofile_page(request):
# 	if request.user.is_authenticated:

# 		return render(request, 'fashionportal/userprofile.html')



	
