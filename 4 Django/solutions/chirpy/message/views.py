from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Chirp


def index(request):

    chirps = Chirp.objects.order_by('-posted_date')[:20]

    context = {
        "chirps": chirps
    }

    return render(request, 'message/index.html', context)


def post(request):
    form = request.POST

    chirp = Chirp()
    chirp.message = form['message']
    chirp.author = form['author']

    chirp.save()

    return HttpResponseRedirect(reverse('index'))


def delete_chirp(request, id):
    chirp = Chirp.objects.get(id=id)
    chirp.delete()

    return HttpResponseRedirect(reverse('index'))
