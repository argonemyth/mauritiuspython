from django.conf import settings

LANGUAGES = getattr(settings, 'LANGUAGES')
LANGUAGE_CODE = getattr(settings, 'LANGUAGE_CODE')

NEWSLETTER_TYPE = getattr(settings, 'NEWLETTER_TYPE', ((1, 'Massmail'),(2, 'Workflow')))
NEWSLETTER_TYPE_MASSMAIL = getattr(settings, 'NEWLETTER_TYPE_MASSMAIL', (1,))
NEWSLETTER_TYPE_WORKFLOW = getattr(settings, 'NEWLETTER_TYPE_WORKFLOW', (2,))

JPEG_QUALITY = getattr(settings, 'JPEG_QUALITY', 75)
