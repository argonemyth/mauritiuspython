from django.conf import settings

LANGUAGES = getattr(settings, 'LANGUAGES')
LANGUAGE_CODE = getattr(settings, 'LANGUAGE_CODE')
JPEG_QUALITY = getattr(settings, 'JPEG_QUALITY', 75)
