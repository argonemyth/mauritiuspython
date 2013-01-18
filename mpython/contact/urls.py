from django.conf import settings
from django.conf.urls.defaults import patterns, url
from contact.views import ContactView
from django.views.generic import TemplateView

template_name = getattr(settings, 'CONTACT_SUCCESS_TEMPLATE', 
                        'contact/success.html')

urlpatterns = patterns('',
    url(r'^$', ContactView.as_view(), name="contact"),
    url(r'^success/$', TemplateView.as_view(template_name=template_name),
        name="contact-success"),
)
