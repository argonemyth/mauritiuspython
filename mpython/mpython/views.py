from django.views.generic import TemplateView
from schedule.models import Event


class HomeView(TemplateView):
    template_name = "base/landing.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeView, self).get_context_data(**kwargs)
        # TODO: Add site activities
        context['recent_activities'] = None
        # Add recent events
        context['recent_events'] = Event.objects.filter().order_by('-start')[:5]
        # Add in recent twitter stream 
        return context

class AboutView(TemplateView):
    template_name = "about.html"
