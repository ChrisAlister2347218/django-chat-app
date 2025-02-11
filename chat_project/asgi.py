import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Set Django settings module before importing anything that uses Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')

# Import after setting DJANGO_SETTINGS_MODULE
import django
django.setup()

from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})

# Bind to the PORT environment variable (used by Render)
port = os.environ.get("PORT", "10000")  # Default to 10000 if PORT is not set
