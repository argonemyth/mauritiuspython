# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, redirect
from django.utils.timezone import now

from userena.contrib.umessages.forms import ComposeForm
from userena import settings as userena_settings

@login_required
def message_compose(request, recipients=None, compose_form=ComposeForm,
                    success_url=None, template_name="umessages/message_form.html",
                    recipient_filter=None, extra_context=None):

    initial_data = dict()

    if recipients:
        username_list = [r.strip() for r in recipients.split("+")]
        recipients = [u for u in User.objects.filter(username__in=username_list)]
        initial_data["to"] = recipients

    form = compose_form(initial=initial_data)
    if request.method == "POST":
        print "Let's see if it gets it"
        form = compose_form(request.POST)
        if form.is_valid():
            requested_redirect = request.REQUEST.get("next", False)

            message = form.save(request.user)
            recipients = form.cleaned_data['to']

            if userena_settings.USERENA_USE_MESSAGES:
                messages.success(request, _('Message is sent.'),
                                 fail_silently=True)

            """
            We don't need other redirection for now
            requested_redirect = request.REQUEST.get(REDIRECT_FIELD_NAME,
                                                     False)

            # Redirect mechanism - we don't need that!
            if requested_redirect: redirect_to = requested_redirect
            elif success_url: redirect_to = success_url
            elif len(recipients) == 1:
                redirect_to = reverse('userena_umessages_detail',
                                      kwargs={'username': recipients[0].username})
            """
            #redirect_to = reverse('userena_umessages_list')
            redirect_to = reverse('userena_umessages_detail',
                                  kwargs={'username': recipients[0].username})
            return redirect(redirect_to)

    if not extra_context: extra_context = dict()
    extra_context["form"] = form
    extra_context["recipients"] = recipients
    return direct_to_template(request,
                              template_name,
                              extra_context=extra_context)

