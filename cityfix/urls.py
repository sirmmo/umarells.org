from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
   
    url(r'^$', 'cityfix.views.index', name='cityfix'),
    url(r'^/data\.geojson$', 'cityfix.views.map', name='cityfix_map'),
    url(r'^/imgs/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/(?P<id>\d*)\.jpg$', 'cityfix.views.image', name='cityfix_img'),
    url(r'^/push/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', 'cityfix.views.push_file', name='cityfix_push_file'),
    url(r'^/push$', 'cityfix.views.push', name='cityfix_push'),
    url(r'^/form\.json$', 'cityfix.views.form', name='cityfix_form'),
    url(r'^/form_meta\.json$', 'cityfix.views.form_meta', name='cityfix_form_meta'),
    
)
