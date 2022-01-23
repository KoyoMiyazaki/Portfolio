from django.urls import path
from . import views

app_name = 'memo'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/<str:pk>/', views.project, name='project'),
    path('update-memo/<str:pk>/', views.update_memo, name='update-memo'),
    path('delete-memo/<str:pk>/', views.delete_memo, name='delete-memo'),
]