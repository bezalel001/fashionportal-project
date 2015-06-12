from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from fashionportal.models import Gallery, Thumbnail, LargePictures, Job, Shop

class ShopListView(ListView):
	model = Shop
	template_name = 'fashionportal/jobs.html'
	context_object_name = 'shops'