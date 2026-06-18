"""
WSGI config for TiendaMascotasWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

# Ensure the root directory is in sys.path before loading Django
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TiendaMascotasWeb.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
app = application
