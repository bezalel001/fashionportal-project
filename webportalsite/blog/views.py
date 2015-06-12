from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import CreateView
from django.forms import ModelForm

# Create your views here.

from blog.models import  BlogEntry
from fashionportal.models import UserProfile

#from blog.forms import BlogEntryForm, BlogAuthorForm, BlogForm



class CreateBlogEntryView(CreateView):
	model = BlogEntry
	fields = ('headline', 'body_text', 'photo',)
	template_name = 'fashionportal/create-blog-entry.html'
	success_url = 'fashionportal:blog'

	def form_valid(self, form):
		form.instance.author = self.request.user.first_name
		return super(CreateBlogEntryView, self).form_valid(form)

	def get_success_url(self):
		return reverse(self.success_url)


# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('pub_date', 'author', 'body_text',)

# def add_comment(request, pk):
#     """Add a new comment."""
#     entry = request.POST

#     if entry.has_key("body_text") and entry["body_text"]:
#         author = "Anonymous"
#         if entry["author"]: 
#         	author = entry["author"]

#         comment = Comment(blog_entry = BlogEntry.objects.get(pk=pk))
#         comment_form = CommentForm(entry, instance=comment)
#         comment_form.fields["author"].required = False

#         comment = comment_form.save(commit=False)
#         comment.author = author
#         comment.save()
#     return HttpResponseRedirect(reverse("fashionportal:blog", args=[pk]))

# def createBlogEntryView(request):
# 	if request.method == 'POST':

# 		blogForm = BlogForm(request.POST)
# 		blogAuthorForm = BlogAuthorForm(request.POST)
# 		blogEntryForm = BlogEntryForm(request.POST)

# 		if blogEntryForm.is_valid() and blogForm.is_valid() and blogAuthorForm.is_valid():
# 			blogForm.save()
# 			blogAuthorForm.save()
# 			blogEntry = blogEntryForm.save(commit=False)


# 			if Blog.objects.all and BlogAuthor.objects.all:
# 				blogEntry.save()
# 			return HttpResponseRedirect(reverse('fashionportal:blog'))

# 		else:
# 			blogEntryForm  = BlogEntryForm()
# 			blogForm = BlogForm()
# 			blogAuthorForm = BlogAuthorForm()
# 			return render(request, 'fashionportal/create-blog-entry.html', {'blogAuthorForm':blogAuthorForm, 'blogForm':blogForm, 'blogEntryForm': blogEntryForm})
# 	else:
# 		blogEntryForm  = BlogEntryForm()
# 		blogForm = BlogForm()
# 		blogAuthorForm = BlogAuthorForm()
# 	return render(request, 'fashionportal/create-blog-entry.html', {'blogEntryForm': blogEntryForm, 'blogForm':blogForm, 'blogAuthorForm': blogAuthorForm})





