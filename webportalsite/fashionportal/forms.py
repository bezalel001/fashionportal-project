from django import forms
from django.forms import ModelForm

from registration.forms import RegistrationForm

from fashionportal.models import UserProfile	


class UserProfileForm(RegistrationForm):
	class Meta:
		model = UserProfile
		fields = ('phone', 'occupation', 'date_of_birth')





# TITLE_CHOICES = (
# 	('MR', 'Mr'),
# 	('MRS', 'Mrs'),
# 	('MS', 'Ms'),
# )

# class AuthorForm(forms.Form):
# 	name = forms.CharField(max_length=100)
# 	title = forms.CharField(max_length= 3, widget=forms.Select(choices=TITLE_CHOICES))
# 	birth_date - forms.DateField(required=False)

# class BookForm(forms.Form):
# 	name = forms.CharField(max_length=100)
# 	authors = forms.ModelMultipleChoiceField(queryset.Author.objects.all())

# class Author(models.Model):
# 	name = models.CharField(max_length=100)
# 	title = models.CharField(max_length=3, choices=TITLE_CHOICES)
# 	birth_date = models.DateField(blank=True, null=True)

# 	def __str__(self):
# 		return self.name

# class Book(models.Model):
# 	name = models.CharField(max_length=100)
# 	authors = models.ManyToManyField(Author)

# class AuthorModelForm(ModelForm):
# 	class Meta:
# 		model = Author
# 		fields = ['name', 'title', 'birth_date']
# class BookModelForm(ModelForm):
# 	class Meta:
# 		model = Book
# 		fields = ['name', 'authors']
