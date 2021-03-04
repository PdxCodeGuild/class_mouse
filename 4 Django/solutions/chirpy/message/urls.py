from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/', views.post, name="post"),
    path('delete/<int:id>/', views.delete_chirp, name="delete_chirp"),
    path('signup/', views.signup_user, name="signup"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout")
]
