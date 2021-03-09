from django.urls import path

from . import views

app_name = "shortener"
urlpatterns = [
    path('', views.index, name="index"),
    path('save/', views.save_url, name="save"),
    path('<str:code>/', views.forward, name="forward")
]
