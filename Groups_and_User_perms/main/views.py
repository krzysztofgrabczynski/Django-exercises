from django.shortcuts import render, HttpResponse, redirect
from .models import BaseModel, Film, Book, Article
from .forms import AddNewForm


def index(request):
    objects = BaseModel.get_all_objects()

    context = {
        'objects': objects
    }
    return render(request, 'index.html', context)

def create_obj(request):
    form = AddNewForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            print('po valid')
            obj_type = form.cleaned_data['type']
            print(obj_type)
            print(BaseModel.TypeChoices.FILM.value)
            if int(obj_type) == BaseModel.TypeChoices.FILM.value:
                print('w film')
                Film.objects.get_or_create(
                    title = form.cleaned_data['title'],
                    description = form.cleaned_data['description'],
                    type = obj_type,
                    price = form.cleaned_data['price'],
                    is_available = form.cleaned_data['is_available'],
                )
            elif int(obj_type) == BaseModel.TypeChoices.BOOK.value:
                print('w book')
                Book.objects.create(
                    title = form.cleaned_data['title'],
                    description = form.cleaned_data['description'],
                    type = obj_type,
                    price = form.cleaned_data['price'],
                    is_available = form.cleaned_data['is_available'],
                )
            elif int(obj_type) == BaseModel.TypeChoices.ARTICLE.value:
                print('w article')
                Article.objects.create(
                    title = form.cleaned_data['title'],
                    description = form.cleaned_data['description'],
                    type = obj_type,
                    price = form.cleaned_data['price'],
                    is_available = form.cleaned_data['is_available'],
                )
    # form.is_valid():
    #     print(form.type)
    #     form.type = 3
    #     print(form.type)
    #     form.save()

            return redirect(index)
    
    return render(request, 'create_obj.html', {'form': form})
