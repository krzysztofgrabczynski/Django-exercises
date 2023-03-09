from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Goal, GoalsList
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    users_goalslist = GoalsList.objects.get(user=request.user)

    context = {
        'goals': users_goalslist.goals_list,
    }
    return render(request, 'home.html', context)

def sign_up(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST or None)
        if user_creation_form.is_valid():
            user = user_creation_form.save()
            GoalsList.objects.create(user=user)
            login(request, user)
            
            return redirect(home)

    user_creation_form = UserCreationForm()
    context = {
        'form': user_creation_form
    }
    return render(request, 'registration/sign-up.html', context) 

@login_required
def add(request):
    if request.method == 'GET':
        goal = request.GET.get('add_goal')
        print(goal)
        if goal:
            Goal.objects.create(
                user=request.user,
                details=goal,
            )

    return redirect(home)
