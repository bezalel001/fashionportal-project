from django.shortcuts import render
from django.contrib.auth.models import User
from fashionportal.models import  PostEntry, UserProfile


def designers_page(request):
	designers_posts = PostEntry.objects.filter(posted_by__occupation="DESIGNER")
	context = {'designers_posts' : designers_posts}
	return render(request, 'fashionportal/fashion-designers.html', context)