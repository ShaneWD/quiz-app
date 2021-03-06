from django.shortcuts import render
from .models import Quiz
from .forms import QuizForm
from django.contrib.auth.decorators import login_required
import random


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
    title_list = []
    answer_list = []
    all_list=[]
    info = Quiz.objects.get(id=pk, author=user)
    for title in info.data.keys():
            title = title.replace("dict_keys(['", "")
            title = title.replace("'])", "")
            answer = info.data[title]['true']
            incorrect = info.data[title]['false']
            title_list.append(title)
            answer_list.append(answer)
            all_list.append(title)
            random_list = []
            random_list.append(answer)
            for i in incorrect:
                random_list.append(i)
            random.shuffle(random_list)
            all_list.append(random_list)
        # title = title ( what is the color of the sky )
        # data = the whole dictionary ( {'true': 'blue', 'false': ['green', 'violet', 'red']} )
        # answer = value with the key of "true" (blue)
        # incorrect = values with the key of "false" (['green', 'violet', 'red'])
    context = {
        #'quiz': quiz,
        'all_list': all_list
    }
    return render(request, "main/detail_view.html", context)