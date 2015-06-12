from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from fashionportal.models import News


class NewsListView(ListView):

 	model = News
 	template_name = 'fashionportal/news.html'
 	context_object_name = 'news_list'

 	def get_query_set(self):
 		queryset = News.objects.all().order_by('-pub_date')
 		return queryset


class NewsDetailView(DetailView):
	model = News
	template_name = 'fashionportal/show-news-details.html'
	context_object_name = 'news'
