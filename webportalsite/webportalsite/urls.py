from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from fashionportal.forms import UserProfileForm
from registration.views import RegistrationView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webportalsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace='auth')),
    #url (r'^accounts/register/$', RegistrationView.as_view (), name = 'registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^fashionportal/', include('fashionportal.urls', namespace='fashionportal')),
    url(r'^blog/', include('blog.urls', namespace='fashionblog')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
