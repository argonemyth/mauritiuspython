# coding=utf-8
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mailblast.models import Newsletter, Subscription, Email, SentLog
from mailblast.tasks import send_newsletter

class NewsletterAdmin(admin.ModelAdmin):
    """
    Admin class for newsletters.
    """
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'active', 'template', 'use_html', 'sender_name',
                    'sender_email', 'date_create', 'date_modify')
    list_editable = ('active', 'template', 'use_html', 'sender_name', 
                     'sender_email')
    list_filter = ('active', )
    date_hierarchy = "date_create"
    ordering = ("-date_create", )


class SubscriptionAdmin(admin.ModelAdmin):
    """
    Admin class for subscription.
    """
    list_display = ('__unicode__', 'subscribed', 'date_create')
    list_editable = ('subscribed', )
    list_filter = ('subscribed', )
    search_fields = ('email', )
    date_hierarchy = 'date_create'
    ordering = ('date_create', )


class EmailAdmin(admin.ModelAdmin):
    """
    Admin class for emails.
    """
    prepopulated_fields = {"slug": ("subject",)}
    list_display = ('__unicode__', 'newsletter', 'composer', 'status', 
                    'date_create', 'date_modify',)
    list_filter = ('newsletter', 'status', )
    date_hierarchy = "date_create"
    ordering = ("-date_create", )

    actions = ['send_emails']

    def send_emails(self, request, queryset):
        """
        queryset is the models that got selected.
        """
        for email in queryset:
            send_newsletter.delay(email)
    send_emails.short_description = _("Send selected emails")


class SentLogAdmin(admin.ModelAdmin):
    """
    Admin class for sent log.
    """
    list_display = ('email', 'to', 'result', 'timestamp', 'log_message')
    list_filter = ('result', )
    date_hierarchy = "timestamp"
    ordering = ("-timestamp", )

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(SentLog, SentLogAdmin)
