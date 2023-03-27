from django.shortcuts import render, HttpResponse, redirect
from .models import BaseModel, Film, Book, Article
from .forms import AddNewForm


def index(request):
    objects = []
    with BaseModel.SubclassesContextManager() as manager:
        for obj in manager:
            objects.extend(obj.objects.all())

    context = {
        'objects': objects
    }
    return render(request, 'index.html', context)

def create_obj(request):
    form = AddNewForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            obj_type = form.cleaned_data['type']
            if int(obj_type) == BaseModel.TypeChoices.FILM.value:
                Film.objects.get_or_create(
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

def edit(request, id):
    pass

def delete(request, id):
    result = None
    with BaseModel.SubclassesContextManager() as manager:
        for obj in manager:
            if not result:
                result = obj.objects.filter(id=id)

    result.delete()
    return redirect(index)