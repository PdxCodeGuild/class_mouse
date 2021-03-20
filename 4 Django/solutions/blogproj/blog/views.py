from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.contrib.auth.models import User

# Create your views here.
from .models import BlogPost


def create_blog(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = request.POST
        title = form['title']
        body = form['body']
        image = request.FILES.get('image', '')

        blog = BlogPost()
        blog.title = title
        blog.body = body
        if image:
            blog.image = image

        user = User.objects.get(id=request.user.id)
        blog.user = user

        blog.save()

        return HttpResponseRedirect(reverse('users:profile'))

    return render(request, 'blog/create.html')


def detail(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)

    if request.method == 'POST' and request.user == blog.user:
        form = request.POST
        title = form['title']
        body = form['body']
        image = request.FILES.get('image', '')

        blog.title = title
        blog.body = body
        if image:
            blog.image = image
        blog.save()

    context = {
        'blog': blog
    }

    return render(request, 'blog/detail.html', context)


def all_posts(request):
    blogs = BlogPost.objects.filter(public=True)
    context = {
        'blogs': blogs
    }

    return render(request, 'blog/posts.html', context)
