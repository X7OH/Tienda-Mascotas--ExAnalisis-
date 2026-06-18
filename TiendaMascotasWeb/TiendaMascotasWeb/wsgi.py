"""
WSGI config for TiendaMascotasWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
import traceback

def application_error(environ, start_response):
    status = '500 Internal Server Error'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    return [traceback.format_exc().encode('utf-8')]

try:
    from django.core.wsgi import get_wsgi_application
    
    # Ensure the root directory is in sys.path
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)
        
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TiendaMascotasWeb.settings')
    application = get_wsgi_application()
    app = application
except Exception as e:
    app = application_error
    application = application_error
