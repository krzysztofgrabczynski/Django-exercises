from django.shortcuts import render, redirect
from .models import Goal, GoalsList
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    users_goalslist = GoalsList.objects.get(user=request.user)
    goals = users_goalslist.goals_list

    f = request.GET.get('filter')
    if f:
        if f == 'Completed':
            goals = list(filter(lambda x: x.is_completed == True, goals))   
        elif f == 'NotCompleted':
            goals = list(filter(lambda x: x.is_completed == False, goals))   

    context = {
        'goals': goals,
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
        if goal:
            Goal.objects.create(
                user=request.user,
                details=goal,
            )

    return redirect(home)

@login_required
def delete(request, id):
    goal = Goal.objects.get(pk=id)
    goal.delete()

    return redirect(home)

@login_required
def check_status_completed(request, id):
    goal = Goal.objects.get(pk=id)
    goal.is_completed = not goal.is_completed
    goal.save()

    return redirect(home)

