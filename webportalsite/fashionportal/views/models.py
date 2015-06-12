from django.shortcuts import render
from fashionportal.models import PostEntry

def models_page(request):
	models_posts = PostEntry.objects.filter(posted_by__occupation="MODEL").order_by('-pub_date')
	context = {'models_posts' : models_posts}
	return render(request, 'fashionportal/models.html', context)