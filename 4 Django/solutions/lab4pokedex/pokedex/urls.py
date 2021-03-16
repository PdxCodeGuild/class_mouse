from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:number>/', views.detail, name="detail"),
    path('api/', views.api_list, name="api_list"),
    path('<int:number>/api/', views.api_detail, name='api_detail')
]
