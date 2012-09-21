from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from views import HomeView, AboutView

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mpython.views.home', name='home'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    # url(r'^mpython/', include('mpython.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Account related
    url(r'^accounts/', include('userena.urls')),

    # For Events
    url(r'^events/', include('schedule.urls')),
)
