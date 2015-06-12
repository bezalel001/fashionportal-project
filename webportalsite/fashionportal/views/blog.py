from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django import forms

from blog.models import BlogEntry, Comment

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.forms import ModelForm

# # class CommentForm(ModelForm):
# # 	class Meta:
# 		model = Comment
# 		fields = ['author', 'body_text']


class CommentForm(forms.Form):
	author = forms.CharField(max_length=255)
	body_text = forms.CharField(max_length=254)

	def clean(self):
		pass



class BlogPostListView(ListView):
	model = BlogEntry
	template_name = 'fashionportal/blog.html'

	def get_queryset(self):
		queryset = BlogEntry.objects.all().order_by('-pub_date')
		return queryset




class BlogPostDetailView(DetailView):
	model = BlogEntry
	form_class = CommentForm
	initial = {'author':'Your name here', 'body_text':'Your Comments here'}
	template_name = 'fashionportal/blog-entry-detail.html'
	context_object_name = 'blogPost'
	

	def get(self, request, *args, **kwargs):
		blogPost = BlogEntry.objects.get(pk=kwargs['pk'])
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form':form, 'blogPost':blogPost})

	def post(self, request, *args, **kwargs):
		blogPost = BlogEntry.objects.get(pk=kwargs['pk'])
		form = self.form_class(request.POST)
		if form.is_valid():
			author = form.cleaned_data['author']
			body_text = form.cleaned_data['body_text']
			comment = Comment(author=author, body_text=body_text)
			

			# comment = form.save(commit=False)
			post = BlogEntry.objects.get(pk=int(kwargs['pk']))
			comment.blog_entry = post
			comment.save()
			return HttpResponseRedirect(reverse('fashionportal:blog_entry_detail', args=self.kwargs['pk']))

		else:
			return render(request, self.template_name, {'form':form, 'blogPost':blogPost})

	def get_queryset(self):
		queryset = BlogEntry.objects.get(pk=self.pk)
		return queryset




	# def get_context_data(self, **kwargs):
	# 	context = super(BlogPostDetailView, self).get_context_data(**kwargs)
	# 	context['form'] = CommentForm
	# 	return context




            
            
        

         
    
