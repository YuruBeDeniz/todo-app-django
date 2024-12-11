from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTasks),
    path('create/', views.addTask),
    path('read/<str:pk>', views.getTask),
    path('update/<str:pk>', views.updateTask),
    path('delete/<str:pk>', views.deleteTask),
]