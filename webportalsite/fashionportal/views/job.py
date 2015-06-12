from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from fashionportal.models import Gallery, Thumbnail, LargePictures, Job

class JobListView(ListView):
	model = Job
	template_name = 'fashionportal/jobs.html'
	



