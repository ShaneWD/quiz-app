from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz
from .forms import QuizForm


def home(request):
    context = {

    }
    return render (request, "main/home.html", context)



def test(request):
    form = QuizForm()
    context = {
        "quizes":Quiz.objects.all(),
        "form": form
    }
    return render(request, "main/test.html", context)

