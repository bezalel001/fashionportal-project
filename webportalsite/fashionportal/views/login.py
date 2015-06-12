from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django import forms


class LoginForm(forms.Form):
	username = forms.CharField(max_length=25)
	password = forms.CharField(max_length=25, widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if not authenticate(username=username, password=password):
			raise forms.ValidationError('Wrong username or password!')
		return self.cleaned_data

def login_page(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password='password')

			if user is not None:
				if user.is_active:
					login(request ,user)
					return HttpResponseRedirect(reverse('fashionportal:profile'))
			else:
				form = LoginForm()
				return render(request, 'fashionportal/login.html',{'form': form})
	else:
		form = LoginForm()
	return render(request, 'fashionportal/login.html', {'form':form})

