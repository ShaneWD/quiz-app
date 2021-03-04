from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz
from .forms import QuizForm
import json

def home(request):
    context = {

    }
    return render (request, "main/home.html", context)



def test(request):
    form = QuizForm()
    # obj = Quiz.objects.filter(data__has_key='What is 2+2?').first().data
    user = request.user
    list_of_keys = []
    for objs in Quiz.objects.filter(author=user):
        list_of_keys.append(objs)

    context = {
        "quizes": Quiz.objects.all(),
        "data": Quiz,
        'obj': objs,
        'list': list_of_keys[1].data,
        "form": form,
    }
    return render(request, "main/test.html", context)

