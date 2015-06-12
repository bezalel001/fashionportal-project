from django import forms
from django.forms import ModelForm

from blog.models import Blog, BlogAuthor, BlogEntry


class BlogEntryForm(ModelForm):

	class Meta:
		model = BlogEntry
		fields = ('headline', 'body_text', )


class BlogForm(ModelForm):

	class Meta:
		model = Blog


class BlogAuthorForm(ModelForm):

	class Meta:
		model = BlogAuthor

