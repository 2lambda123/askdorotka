from django.conf.urls.defaults import *
from askdorotka.gallery.views import random_pic, random_gallery

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import os

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', \
        {'document_root': os.path.join(os.path.dirname(__file__), 'images')}),
    (r'^random/(.*)/$', random_pic),
    (r'^gallery/(.*)/(\d{1,2})/$', random_gallery),
    # Example:
    # (r'^imagesearch/', include('imagesearch.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
