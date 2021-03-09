import random
import string

from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse

from .models import ShortenedURL
# Create your views here.


def index(req):
    urls = ShortenedURL.objects.order_by('-counter')

    highlight_code = req.GET.get('highlight', '')
    context = {
        'urls': urls,
        'highlight': highlight_code
    }
    return render(req, 'shortener/index.html', context)


def save_url(req):
    try:
        shortend_url = ShortenedURL.objects.get(url=req.POST['url'])
        return HttpResponseRedirect(reverse('shortener:index') + f'?highlight={shortend_url.code}')
    except:
        characters = string.ascii_letters + string.digits
        code = ''
        while len(code) < 5:
            code += random.choice(characters)

        form = req.POST
        url = form['url']

        shortend_url = ShortenedURL(code=code, url=url)
        # shortend_url.code = code
        # shortend_url.url = url
        shortend_url.save()

        return HttpResponseRedirect(reverse('shortener:index'))


def forward(req, code):
    if len(code) != 5:
        return HttpResponseRedirect(reverse('shortener:index'))

    shortened_url = get_object_or_404(ShortenedURL, code=code)
    shortened_url.counter += 1
    shortened_url.save()

    url = shortened_url.url

    return redirect(url)
