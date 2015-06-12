from django.shortcuts import render
from fashionportal.models import  PostEntry

def tailors_page(request):
	tailors_posts = PostEntry.objects.filter(posted_by__occupation="TAILOR").order_by('-pub_date')
	context = {'tailors_posts' : tailors_posts}
	return render(request, 'fashionportal/tailors.html', context)