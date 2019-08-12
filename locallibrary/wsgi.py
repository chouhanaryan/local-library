"""
WSGI config for locallibrary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')

<<<<<<< HEAD
application = get_wsgi_application()
=======
application = get_wsgi_application()
>>>>>>> 966a25c7653f18d6992532af252992869a4dcce5
