# coding=utf-8
from django.contrib import admin

from mailblast.models import Newsletter, Subscription, Email


class NewsletterAdmin(admin.ModelAdmin):
    """
    Admin class for newsletters.
    """
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'active', 'newsletter_type', 'sender_name',
                    'sender_email', 'date_create', 'date_modify')
    list_editable = ('active', 'newsletter_type', 'sender_name', 'sender_email')
    list_filter = ('active', 'newsletter_type')
    date_hierarchy = "data_create"
    ordering = ("-date_create", )


class SubscriptionAdmin(admin.ModelAdmin):
    """
    Admin class for subscription.
    """
    list_display = ('__unicode__', 'subscribed', 'date_create')
    list_editable = ('subscribed')
    list_filter = ('subscribed')
    search_fields = ('email')
    date_hierarchy = 'data_create'
    ordering = ('date_create', )


class EmailAdmin(admin.ModelAdmin):
    """
    Admin class for emails.
    """
    prepopulated_fields = {"slug": ("subject",)}
    list_display = ('__unicode__', 'composer', 'status', 'date_create', 
                    'date_modify',)
    list_filter = ('status', )
    date_hierarchy = "data_create"
    ordering = ("-date_create", )

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Email, EmailAdmin)
