from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RemoteServer, ServerMetrics
from .utils.remote_fetcher import fetch_linux_metrics, fetch_windows_metrics

@api_view(['POST'])
def fetch_and_update_metrics(request, server_id):
    try:
        server = RemoteServer.objects.get(id=server_id)
        metrics = fetch_linux_metrics(server) if server.os_type == 'Linux' else fetch_windows_metrics(server)

        ServerMetrics.objects.update_or_create(
            server=server,
            defaults=metrics
        )
        return Response({"status": "success", "metrics": metrics})
    except Exception as e:
        return Response({"status": "error", "error": str(e)})
    



def dashboard(request):
    metrics = ServerMetrics.objects.select_related('server').all()
    return render(request, 'dashboard.html', {'metrics': metrics})



def fetch_metrics(request, server_id):
    # Sample dummy response (replace with actual logic later)
    data = {
        "server_id": server_id,
        "cpu_usage": "25%",
        "disk_space": "120 GB Free",
        "status": "Online"
    }
    return JsonResponse(data)


