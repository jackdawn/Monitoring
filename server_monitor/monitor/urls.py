from django.urls import path
from .views import fetch_and_update_metrics, dashboard_view
from django.urls import path
from .views import dashboard_view, fetch_and_update_metrics

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('fetch-metrics/<int:server_id>/', fetch_and_update_metrics),
    path('fetch-metrics/<int:server_id>/', views.fetch_metrics, name='fetch_metrics'),
]

