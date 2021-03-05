from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz
from .forms import QuizForm
from django.contrib.auth.decorators import login_required
import json


def home(request):
    context = {

    }
    return render (request, "main/home.html", context)


@login_required
def the_list(request):
    user = request.user
    a_list = []
    for info in Quiz.objects.filter(author = user):
        info1 = str(info.data.keys()).replace("dict_keys(['", "")
        info1 = info1.replace("'])", "")
        data = info.data[info1]
        answer = info.data[info1]['true']
        incorrect = info.data[info1]['false']
        a_list.append(info1)
        # info1 = title ( what is the color of the sky )
        # data = the whole dictionary ( {'true': 'blue', 'false': ['green', 'violet', 'red']} )
        # answer = value with the key of "true" (blue)
        # incorrect = values with the key of "false" (['green', 'violet', 'red'])

    
    context = {
        "quizes": Quiz.objects.filter(author = user),
        "data": a_list
    }
    
    return render(request, "main/quiz_list.html", context)


@login_required
def view(request, pk):
    user = request.user
    quiz = Quiz.objects.get(id=pk, author=user)
    context = {
        'quiz': quiz
    }
    return render(request, "main/detail_view.html", context)