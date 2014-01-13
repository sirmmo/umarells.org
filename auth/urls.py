from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
   
    
    url(r'^/token/get$', 'auth.views.get_token', name='cityfix_map'),
    url(r'^/token/verify$', 'auth.views.verify_token', name='cityfix_form_meta'),
    
)
