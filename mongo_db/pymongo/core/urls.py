from django.urls import path

from app import views as app_views 

urlpatterns = [
    path('posts/', app_views.list_posts, name="list_posts"),
    path('post/<id>/', app_views.get_post, name="post_detail"),
    path('add/', app_views.add_post, name="add_post"),
]
