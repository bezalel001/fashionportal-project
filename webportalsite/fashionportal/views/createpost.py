from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from fashionportal.models import UserProfile, PostEntry, occupations



class CreatePostView( SuccessMessageMixin, CreateView):
	model = PostEntry
	fields = ('description', 'photo')
	template_name = 'fashionportal/create-post.html'
	success_url = 'fashionportal:profile'
	success_message =  'Profile and description posted.'


	def form_valid(self, form):
		form.instance.posted_by = self.request.user.userprofile
		return super(CreatePostView, self).form_valid(form)

	def get_success_url(self):
		return reverse(self.success_url, args=(self.request.user.username,) )

	



class EditPostView(UpdateView):
	model = PostEntry
	fields = ('description', 'photo')
	template_name = 'fashionportal/edit-post.html'
	success_url = 'fashionportal:profile'

	def get_success_url(self):
		return reverse(self.success_url, args=(self.request.user.username, ))


class DeletePostView(DeleteView):
	model = PostEntry
	fields = ('description', 'photo')
	template_name = 'fashionportal/delete-post.html'
	success_url = 'fashionportal:profile'
	context_object_name = 'post_entry'

	def get_success_url(self):
		return reverse(self.success_url, args=(self.request.user.username, ))



# class CreatePostModelForm(ModelForm):
# 	class Meta:
# 		model = PostEntry
# 		exclude = ('cropping',)

# def create_post_page(request):
# 	if request.method == 'POST':
# 		form = CreatePostModelForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect(reverse(occupations[form.cleaned_data['occupation']]))
# 	else:
# 		form = CreatePostModelForm()
# 		return render(request, 'fashionportal/create-post.html', {'form' : form})