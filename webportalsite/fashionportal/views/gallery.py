from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from fashionportal.models import Gallery, Thumbnail, LargePictures

class GalleryView(ListView):
	model = Gallery
	template_name = 'fashionportal/gallery.html'

	


class GalleryListView(ListView):
	model = Gallery
	template_name = 'fashionportal/gallery-list.html'
	context_object_name = 'gallery_photos'

	def get_queryset(self):		
		queryset = Gallery.objects.get(id=int(self.kwargs['pk']))
		return queryset

	

class ShowPhotoDetailView(DetailView):
	model = Thumbnail
	template_name = 'fashionportal/show-photo.html'
	context_object_name = 'photo'

class VideosGalleryListView(ListView):
	model = Thumbnail
	template_name = 'fashionportal/videos.html'

