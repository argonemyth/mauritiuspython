from django.conf.urls import patterns, include, url

from accounts import views as messages_views

urlpatterns = patterns('',
    url(r'^messages/compose/$',
        messages_views.message_compose,
        name='userena_umessages_compose'),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
)
