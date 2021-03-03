from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/', views.post, name="post"),
    path('delete/<int:id>/', views.delete_chirp, name="delete_chirp")
]
