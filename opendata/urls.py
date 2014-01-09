from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'opendata.views.index', name='opendata'),
    url(r'^/add$', 'opendata.views.add_internet_resource', name='add_opendata'),
    url(r'^/remove$', 'opendata.views.remove_interet_resource', name='del_opendata'),
    url(r'^/evaluate$', 'opendata.views.evaluate_internet_resource', name='eval_opendata'),
    url(r'^/(?P<resource>\d+)$', 'opendata.views.show_resource', name='show_opendata'),
    url(r'^/data\.csv$', 'opendata.views.show_resource', name='get_opendata'),
)
