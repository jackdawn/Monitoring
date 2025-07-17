# Monitoring

python3 -m venv venv
source venv/bin/activate
pip install django
django-admin startproject server_monitor
cd server_monitor
python manage.py startapp monitor
