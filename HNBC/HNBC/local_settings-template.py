# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MACHINE_NAME = 'Door'
MACHINE_ID = 0

# Example (domain name = localhost)
RECAPTCHA_PUBLIC_KEY = '6LcDeOoSAAAAAHXYI1V1noRNM9C7hkVp1tJWrhHi'
RECAPTCHA_PRIVATE_KEY = '6LcDeOoSAAAAAGLMcUnCU00L8IVfay6xmb8W6pnL'
RECAPTCHA_USE_SSL = True

# Auth servers config
upstream_servers = {
    # Master server
    'master': {
        'url': 'http://drupalinstall.example.org',
        'login': {
            # Username and password
            'username': 'frontdoor',
            'password': 'frontdoorpass',

            # These might change with Drupal versions
            'uri': '/user/login',
            'username_form_key': 'name',
            'password_form_key': 'pass',
            'login_form_id': 'user_login',
        },
    },
}

ALLOWED_HOSTS = [
    'localhost',
]

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'


"""
Two things are wrong with Django's default `SECRET_KEY` system:

1. It is not random but pseudo-random
2. It saves and displays the SECRET_KEY in `settings.py`

This snippet
1. uses `SystemRandom()` instead to generate a random key
2. saves a local `secret.txt`

The result is a random and safely hidden `SECRET_KEY`.

"""
try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(BASE_DIR, '../secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            import random
            SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)

