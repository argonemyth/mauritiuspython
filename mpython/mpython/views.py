from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "base/landing.html"

class AboutView(TemplateView):
    template_name = "about.html"

class WorkshopView(TemplateView):
    template_name = "workshop.html"
