from django.http import HttpResponse
from bson import ObjectId
from django.utils import timezone
from django.shortcuts import render
 
from app.models import post_collection
from app.forms import AddPost


def list_posts(request):
    posts = list(post_collection.find())
    for post in posts:
        post['id'] = str(post.pop('_id')) 
    context = {'posts': posts}
    return render(request, "post_list.html", context)

def get_post(request, id):
    post = post_collection.find_one({"_id": ObjectId(id)})
    context = {'post': post}
    return render(request, "post_detail.html", context)
    
def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            post_data = {
                "title": cleaned_data["title"],
                "visible": cleaned_data["visible"],
                "created_at": timezone.now()
            }
            post_collection.insert_one(post_data)
            return HttpResponse({"success": "Post created successfully"})
        else:
            return HttpResponse({"errors": form.errors})   
    
    elif request.method == "GET":
        form = AddPost()
        context = {'form': form}
        return render(request, "add_post.html", context)