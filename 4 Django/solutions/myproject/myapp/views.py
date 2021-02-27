from django.shortcuts import render
from .models import BlogPost

# Create your views here.


def index(request):

    blog_posts = BlogPost.objects.all()

    context = {
        "blog_posts": blog_posts
    }
    return render(request, 'myapp/index.html', context)
