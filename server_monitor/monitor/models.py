from django.db import models

class RemoteServer(models.Model):
    OS_CHOICES = (('Linux', 'Linux'), ('Windows', 'Windows'))

    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    os_type = models.CharField(max_length=10, choices=OS_CHOICES)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)  # Encrypt in production

    def __str__(self):
        return self.name


class ServerMetrics(models.Model):
    server = models.OneToOneField(RemoteServer, on_delete=models.CASCADE)
    cpu_utilization = models.CharField(max_length=100, null=True, blank=True)
    disk_space = models.CharField(max_length=100, null=True, blank=True)
    idle_time = models.CharField(max_length=100, null=True, blank=True)
    last_write_time = models.CharField(max_length=100, null=True, blank=True)
    last_write_path = models.CharField(max_length=255, null=True, blank=True)
    last_logged_in_users = models.TextField(null=True, blank=True)
    last_logged_in_time = models.CharField(max_length=100, null=True, blank=True)
    last_app_event_time = models.CharField(max_length=100, null=True, blank=True)

    updated_on = models.DateTimeField(auto_now=True)
