from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import BaseModel, Film, Book, Article
from .forms import AddNewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def sign_up(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(index)

    return render(request, 'registration/sign_up.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            
            return redirect(index)

    return render(request, 'registration/login.html')

@login_required
def logout_user(request):
    logout(request)

    return redirect(index)

@login_required
def index(request):
    objects = []
    with BaseModel.SubclassesContextManager() as manager:
        for obj in manager:
            objects.extend(obj.objects.all())

    context = {
        'objects': objects
    }
    return render(request, 'index.html', context)

@login_required
def create_obj(request):
    form = AddNewForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            obj_type = form.cleaned_data['type']
            if int(obj_type) == BaseModel.TypeChoices.FILM.value:
                Film.objects.create(
                    title = form.cleaned_data['title'],
                    description = form.cleaned_data['description'],
                    type = obj_type,
                    price = form.cleaned_data['price'],
                    is_available = form.cleaned_data['is_available'],
                )
            elif int(obj_type) == BaseModel.TypeChoices.BOOK.value:
                Book.objects.create(
                    title = form.cleaned_data['title'],
                    description = form.cleaned_data['description'],
                    type = obj_type,
                    price = form.cleaned_data['price'],
                    is_available = form.cleaned_data['is_available'],
                )
            elif int(obj_type) == BaseModel.TypeChoices.ARTICLE.value: 
                Article.objects.create(
                    title = form.cleaned_data['title'],
                    description = form.cleaned_data['description'],
                    type = obj_type,
                    price = form.cleaned_data['price'],
                    is_available = form.cleaned_data['is_available'],
                )

            return redirect(index)
    
    return render(request, 'create_obj.html', {'form': form})

@login_required
def edit(request, id):
    result = None
    with BaseModel.SubclassesContextManager() as manager:
        for obj in manager:
            if not result:
                result = obj.objects.filter(id=id).first()

    get_obj = get_object_or_404(result.__class__, pk=id)
    form = AddNewForm(request.POST or None)
    form.set_instance(get_obj)

    if request.method == 'POST':
        if form.is_valid():
            obj_type = form.cleaned_data['type']
            if int(obj_type) == BaseModel.TypeChoices.FILM.value:
                Film.objects.update(
                    title = form.cleaned_data['title'],
                    description = form.cleaned_data['description'],
                    type = obj_type,
                    price = form.cleaned_data['price'],
                    is_available = form.cleaned_data['is_available'],
                )
            elif int(obj_type) == BaseModel.TypeChoices.BOOK.value:
                Book.objects.update(
                    title = form.cleaned_data['title'],
                    description = form.cleaned_data['description'],
                    type = obj_type,
                    price = form.cleaned_data['price'],
                    is_available = form.cleaned_data['is_available'],
                )
            elif int(obj_type) == BaseModel.TypeChoices.ARTICLE.value:
                Article.objects.update(
                    title = form.cleaned_data['title'],
                    description = form.cleaned_data['description'],
                    type = obj_type,
                    price = form.cleaned_data['price'],
                    is_available = form.cleaned_data['is_available'],
                )

            return redirect(index)
    
    return render(request, 'edit_obj.html', {'form': form})

@login_required
def delete(request, id):
    result = None
    with BaseModel.SubclassesContextManager() as manager:
        for obj in manager:
            if not result:
                result = obj.objects.filter(id=id).first()

    result.delete()
    return redirect(index)
