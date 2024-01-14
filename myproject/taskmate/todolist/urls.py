from django.urls import path
from todolist import views

urlpatterns = [
    path('a', views.todolist ,name='todolist'),
]
