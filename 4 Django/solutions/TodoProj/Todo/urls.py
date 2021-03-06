from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('save/', views.save_todos, name="add_todo"),
    path('complete/<int:todo_id>/', views.complete, name="complete"),
    path('delete/<int:todo_id>/', views.delete, name="delete")
]
