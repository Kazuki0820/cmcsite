from django.contrib import admin
from django.conf import settings
from django.urls import path, include
import django_on_heroku
import dj_database_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apisite.urls')),
]
