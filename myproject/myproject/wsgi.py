"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import threading

from django.core.wsgi import get_wsgi_application

from notification.servicer import serve

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

server_thread = threading.Thread(target=serve, daemon=True)
server_thread.start()
application = get_wsgi_application()
