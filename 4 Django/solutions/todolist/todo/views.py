from django.http.response import JsonResponse
from django.shortcuts import render
import json

# Create your views here.

from .models import TodoItem, Priority


def index(request):
    return render(request, 'todo/index.html')


def todos(request):
    # todo_items = TodoItem.objects.all()
    # output = []
    # for todo in todo_items:
    #     output.append({
    #         'text': todo.text,
    #         'priority': todo.priority.name,
    #         'created_date': todo.created_date,
    #         'completed_date': todo.completed_date
    #     })

    todo_items = TodoItem.objects.order_by('-priority__order', '-created_date').values(
        'text', 'priority__name', 'completed_date')
    output = list(todo_items)

    return JsonResponse(output, safe=False)


def priorities(request):
    prioritys = Priority.objects.order_by('-order').values()
    output = list(prioritys)
    return JsonResponse(output, safe=False)


def save_todo(request):
    data = json.loads(request.body)

    priority = Priority.objects.get(id=data['priorityID'])
    todo = TodoItem()
    todo.text = data['todoText']
    todo.priority = priority
    todo.save()

    return JsonResponse({'message': 'ok'})
