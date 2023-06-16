from django.urls import path
from . import views

app_name = 'apisite'

urlpatterns = [
    path('', views.index, name='index')
]