from django.shortcuts import render


from fashionportal.models import Event


def events_page(request):
	events = Event.objects.all()
	return render(request, 'fashionportal/events.html', {'events': events})