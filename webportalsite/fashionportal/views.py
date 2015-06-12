from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import RegistrationForm
from .models import UserProfile

# Create your views here.

# Registration 

def registration(request):
	# If this is a post request, we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = RegistrationForm(request.POST)
		# check whether the form is valid adn place the form data in its cleaned_data attribute
		if form.is_valid():
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data["last_name"]
			email = form.cleaned_data["email"]
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			new_user = UserProfile(name=first_name + " " + last_name, \
				username=username, password=password, email=email)
			return HttpResponseRedirect(reverse('home'))
	else:
		form = RegistrationForm()
	return render(request, 'fashionportal/register.html', {'form': form})










