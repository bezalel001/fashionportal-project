from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth.models import User


from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login

from registration import signals
from registration.users import UserModel

from fashionportal.models import UserProfile, OCCUPATION_CHOICES
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationForm



class SignupForm(RegistrationForm):

	occupation = forms.CharField(widget=forms.Select(choices=OCCUPATION_CHOICES), label="Occupation")


class FashionPortalRegistrationView(RegistrationView):
	form_class = SignupForm
	success_url = '/fashionportal/'

	def register(self, request, **cleaned_data):
		first_name, last_name = cleaned_data['first_name'], cleaned_data['last_name']
		username, email, password = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
		occupation = cleaned_data['occupation']
		user = User.objects.create_user(username, email, password)
		user.is_active = True
		user.first_name = first_name
		user.last_name = last_name
		user.save()
		profile = UserProfile(user=user, occupation=occupation)
		profile.save()
		new_user = authenticate(username=username, password=password)
		login(request, new_user)
		signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
		return new_user

		def get_success_url(self, request, user):
			return self.success_url



	# def get_form_class(self):
	# 	return form_class



# def signup_page(request):
# 	if request.method == "POST":
# 		form = SignupForm(request.POST)
# 		if form.is_valid():
# 			first_name = form.cleaned_data['first_name']
# 			last_name = form.cleaned_data['last_name']
# 			login = form.cleaned_data['login']
# 			password = form.cleaned_data['password']
# 			email = form.cleaned_data['email']
# 			occupation = form.cleaned_data['occupation']
# 			new_user = User.objects.create_user(username=login, email=email, password=password)
# 			new_user.first_name = first_name
# 			new_user.last_name = last_name
# 			new_user.is_active = True
# 			new_user.save()
# 			new_member = UserProfile(user=new_user, occupation=occupation)
# 			new_member.save()
# 		return HttpResponseRedirect(reverse('fashionportal:login'))
# 	else:
# 		form = SignupForm()
# 	return render(request, 'fashionportal/signup.html',{'form':form})