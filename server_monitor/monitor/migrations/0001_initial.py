# Generated by Django 5.2.4 on 2025-07-18 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ip', models.GenericIPAddressField()),
                ('os_type', models.CharField(choices=[('Linux', 'Linux'), ('Windows', 'Windows')], max_length=10)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ServerMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_utilization', models.CharField(blank=True, max_length=100, null=True)),
                ('disk_space', models.CharField(blank=True, max_length=100, null=True)),
                ('idle_time', models.CharField(blank=True, max_length=100, null=True)),
                ('last_write_time', models.CharField(blank=True, max_length=100, null=True)),
                ('last_write_path', models.CharField(blank=True, max_length=255, null=True)),
                ('last_logged_in_users', models.TextField(blank=True, null=True)),
                ('last_logged_in_time', models.CharField(blank=True, max_length=100, null=True)),
                ('last_app_event_time', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('server', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='monitor.remoteserver')),
            ],
        ),
    ]
