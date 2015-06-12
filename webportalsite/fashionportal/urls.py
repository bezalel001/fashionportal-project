from django.conf.urls import patterns, include, url

from fashionportal.views.blog import BlogPostListView, BlogPostDetailView

from fashionportal import views
#from fashionportal.views.userprofile import ProfilePageView
from fashionportal.views.editprofile import EditProfileView
from fashionportal.views.gallery import GalleryListView, ShowPhotoDetailView, VideosGalleryListView, GalleryView
from fashionportal.views.news import NewsListView, NewsDetailView
from fashionportal.views.signup import FashionPortalRegistrationView
from fashionportal.views.createpost import CreatePostView, EditPostView, DeletePostView
from fashionportal.views.shop import ShopListView
from fashionportal.views.job import JobListView



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webportalsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'fashionportal.views.index.home_page', name='home'),
    url(r'^fashion-designers$', 'fashionportal.views.designers.designers_page', name='designers'), 
    url(r'^fashion-tailors$', 'fashionportal.views.tailors.tailors_page', name='tailors'), 
    url(r'^fashion-photographers$', 'fashionportal.views.photographers.photographers_page', name='photographers'), 
    url(r'^fashion-models$', 'fashionportal.views.models.models_page', name='models'), 
    url(r'^fashion-news$', NewsListView.as_view(), name='news'), 
    url(r'^fashion-events$', 'fashionportal.views.events.events_page', name='events'),   
    url(r'^fashion-blog$', BlogPostListView.as_view(), name='blog'), 
    url(r'^fashion-blog-post-(?P<pk>\d+)$', BlogPostDetailView.as_view(), name='blog_entry_detail'), 
    url(r'^fashion-gallery-list-(?P<pk>\d+)$', GalleryListView.as_view(), name='gallery_list'), 
    url(r'^fashion-signup$', FashionPortalRegistrationView.as_view(), name='signup'),
    url(r'^fashion-login$', 'fashionportal.views.login.login_page', name='login'),
    url(r'^fashion-logout$', 'fashionportal.views.logout.logout_page', name='logout'),
    #url(r'^fashion-userprofile/(?P<username>\w+)/$', ProfilePageView.as_view(), name='profile'),
    url(r'^fashion-create-post$', CreatePostView.as_view(), name='createpost'),
    url(r'^fashion-edit-profile/(?P<username>\w+)$', EditProfileView.as_view(), name='edit-profile'),
    url(r'^fashion-gallery-photo/(?P<pk>\d+)/$', ShowPhotoDetailView.as_view(), name='showphoto'),
    url(r'^ fashion-news-detail/(?P<pk>\d+)/$', NewsDetailView.as_view(), name='newsdetail'),
    url(r'^fashion-userprofile/(?P<username>\w+)/$', 'fashionportal.views.userprofile.userprofile_page', name='profile'),
    url(r'^fashion-gallery-videos$', VideosGalleryListView.as_view(), name='videos'), 
    url(r'^fashion-profile-post-edit/(?P<pk>\d+)/$', EditPostView.as_view(), name='editpost'),
    url(r'^fashion-profile-post-delete/(?P<pk>\d+)/$', DeletePostView.as_view(), name='deletepost'),
    
    url(r'^fashion-gallery$', GalleryView.as_view(), name='gallery'),
    url(r'^fashion-shops$', ShopListView.as_view(), name='shops'), 
    url(r'^fashion-jobs$', JobListView.as_view(), name='jobs'),

)
