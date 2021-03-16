from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Pokemon


def index(request):
    pokemon = Pokemon.objects.all()
    context = {
        'pokemon': pokemon
    }
    return render(request, 'pokedex/index.html', context)


def detail(request, number):
    pokemon = get_object_or_404(Pokemon, number=number)
    context = {
        'pokemon': pokemon
    }
    return render(request, 'pokedex/detail.html', context)


def api_list(request):
    pokemon = Pokemon.objects.all()
    response = {'data': []}
    for mon in pokemon:
        response['data'].append({
            'name': mon.name,
            'number': mon.number,
            'height': mon.height,
            'weight': mon.weight,
            'image_front': mon.image_front,
            'image_back': mon.image_back
        })
    return JsonResponse(response)


def api_detail(request, number):
    pokemon = get_object_or_404(Pokemon, number=number)
    db_types = pokemon.types.all()
    types = []
    for type in db_types:
        types.append(type.name)
    response = {
        'name': pokemon.name,
        'number': pokemon.number,
        'height': pokemon.height,
        'weight': pokemon.weight,
        'image_front': pokemon.image_front,
        'image_back': pokemon.image_back,
        'types': types
    }

    return JsonResponse(response)
