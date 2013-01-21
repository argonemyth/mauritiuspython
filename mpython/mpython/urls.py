from django.conf.urls import patterns, include, url
from django.views.generic import ListView, TemplateView
from django.utils.timezone import now

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from views import HomeView, AboutView
from schedule.models import Event

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mpython.views.home', name='home'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contribution/$', TemplateView.as_view(template_name='contribution.html'), name='contribute'),

    # url(r'^mpython/', include('mpython.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Account related
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('userena.urls')),

    # For Events
    url(r'^meetups/', ListView.as_view(
        model = Event,
        queryset = Event.objects.filter(calendar__slug='meetups')
                        .filter(end__gt=now()).order_by('start'),
        template_name = "meetup_list.html",
        context_object_name = "meetup_list",
    ), name="meetups"),
    url(r'^workshops/', ListView.as_view(
        model = Event,
        queryset = Event.objects.filter(calendar__slug='workshops')
                        .filter(end__gt=now()).order_by('start'),
        template_name = "workshop_list.html",
        context_object_name = "workshop_list",
    ), name="workshops"),
    url(r'^events/', include('schedule.urls')),
    url(r'^reserve/', include('django_reservations.urls')),
    
    # contact
    url(r'^contact/', include('contact.urls')),
)
