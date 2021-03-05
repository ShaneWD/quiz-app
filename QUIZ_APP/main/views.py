from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz
from .forms import QuizForm
from django.contrib.auth.decorators import login_required

def home(request):
    context = {

    }
    return render (request, "main/home.html", context)


@login_required
def the_list(request):
    user = request.user
    context = {
        "quizes": Quiz.objects.filter(author = user),
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