from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.index', name='index'),

    url(r'^opendata$', include("opendata.urls")),
    url(r'^cityfix/', include("cityfix.urls")),

    url(r'^forum$', 'forum.views.index', name='forum'),

    url(r'^signup$', 'umarells.views.signup', name='presignup'),
    url(r'^accounts/profile/$', 'core.views.profile', name='profile'),
    url(r'^accounts/(?P<username>[\w\d\.]+)/$', 'core.views.profile', name='profile'),

    url('', include('social.apps.django_app.urls', namespace='social')),
    # url(r'^umarells/', include('umarells.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
