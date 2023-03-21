from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('send_email/', views.send_email, name='send_email'),
    path('send_email_v2/', views.send_email_v2, name='send_email_v2'),
    path('send_email_with_attachments/', views.send_email_with_attachments, name='send_email_with_attachments'),
]
