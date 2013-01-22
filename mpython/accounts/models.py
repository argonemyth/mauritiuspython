from django.db import models
from django.contrib.auth.models import User 
from django.utils.translation import ugettext_lazy as _
from userena.models import UserenaLanguageBaseProfile 

class Profile(UserenaLanguageBaseProfile):
    GENDER_CHOICES = ( 
        (1, _('Male')),
        (2, _('Female')),
    ) 

    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')
    bio = models.TextField(_('bio'), blank=True, null=True)
    show_email = models.BooleanField(_('show email?'), blank=True, default=False,
                                     help_text= _("Don't select it if you don't\
                                      want to show your email on the profile."))
    website = models.URLField(_('website'), blank=True, verify_exists=False)
    irc_nick = models.CharField(_('IRC nick'), blank=True, null=True,
                                max_length=100, help_text=_("on freenode!"))
    twitter = models.CharField(_('Twitter username'), max_length=100,
                               blank=True, null=True)
    skype_nick = models.CharField(_('Skype nick'), max_length=100, blank=True,
                                  null=True)
    gender = models.PositiveSmallIntegerField(_('gender'),
                                              choices=GENDER_CHOICES,
                                              blank=True, null=True)
    birth_date = models.DateField(_('birth date'), blank=True, null=True)
