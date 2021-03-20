from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('create/', views.create_blog, name="create"),
    path('detail/<int:blog_id>/', views.detail, name="detail"),
    path('posts/', views.all_posts, name="posts"),
]
