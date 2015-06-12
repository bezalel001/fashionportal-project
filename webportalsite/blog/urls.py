from django.conf.urls import patterns, include, url
from blog.views import CreateBlogEntryView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webportalsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', CreateBlogEntryView.as_view(), name='entry'),
)
