from django.contrib import admin
from .models import RemoteServer, ServerMetrics  # Import your models

# Register them
admin.site.register(RemoteServer)
admin.site.register(ServerMetrics)
