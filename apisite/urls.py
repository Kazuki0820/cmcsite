from django.urls import path
from . import views
import django_on_heroku
import dj_database_url

app_name = 'apisite'

urlpatterns = [
    path('', views.index, name='index')
]