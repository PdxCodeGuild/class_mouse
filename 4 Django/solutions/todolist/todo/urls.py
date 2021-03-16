from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('todos/', views.todos, name='todos'),
    path('priorities/', views.priorities, name="priorities"),
    path('save_todo/', views.save_todo, name="save_todo"),
    path('complete_todo/', views.complete_todo, name="complete_todo"),
    path('delete_todo/', views.delete_todo, name="delete_todo")
]
