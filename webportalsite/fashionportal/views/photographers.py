from django.shortcuts import render
from fashionportal.models import Photographer, PostEntry

def photographers_page(request):
	photographers_posts = PostEntry.objects.filter(posted_by__occupation="PHOTOGRAPHER").order_by('-pub_date')
	context = {'photographers_posts' : photographers_posts}
	return render(request, 'fashionportal/photographers.html', context)