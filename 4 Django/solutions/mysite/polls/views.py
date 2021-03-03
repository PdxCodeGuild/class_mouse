from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# Create your views here.


def index(request):
    questions = Question.objects.order_by('-pub_date')
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)


def detail(request, id):
    question = get_object_or_404(Question, id=id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


def results(request, id):
    question = get_object_or_404(Question, id=id)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)


def vote(request, id):
    selected_choice = request.POST['choice']
    choice = get_object_or_404(Choice, id=selected_choice)
    choice.votes += 1
    choice.save()

    return HttpResponseRedirect(reverse('polls:detail', args=(id,)))
