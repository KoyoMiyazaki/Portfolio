from django.urls import path
from . import views

app_name = 'memo'
urlpatterns = [
    path('', views.index, name='index'),
]