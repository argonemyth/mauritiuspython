# Twitter settings file.
"""
These twitter settings should not be edited directly.
Instead, overwrite them in the main project's setting file.
"""
from django.conf import settings

# The name of the Twitter user.
TWITTER_USER = getattr(settings, 'TWITTER_USER', None)

# The number of tweets to be pulled. Defaults to 20.
TWITTER_NUMTWEETS = getattr(settings, 'TWITTER_NUMTWEETS', 10)

# The number of seconds for which tweets should be stored in the cache.
# Defaults to 3 minutes.
TWITTER_TIMEOUT = getattr(settings, 'TWITTER_TIMEOUT', 180)
