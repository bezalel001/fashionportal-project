from django.shortcuts import render
from fashionportal.models import Event, News, Gallery

def home_page(request):
	 
	latest_event = Event.objects.all()
	latest_news = News.objects.all()
	latest_gallery = Gallery.objects.all()
	if len(latest_event) > 0:
		latest_event = latest_event[0]
	else:
		latest_event = None
	if len(latest_news) > 0:
		latest_news = latest_news[0]
	else:
		latest_news = None
	if len(latest_gallery) > 0:
		latest_gallery = latest_gallery[0]
	else:
		latest_gallery = None
		
	context = {
		'latest_gallery': latest_gallery,
		'latest_news': latest_news,
		'latest_event': latest_event
	}
	return render(request, 'fashionportal/index.html', context)