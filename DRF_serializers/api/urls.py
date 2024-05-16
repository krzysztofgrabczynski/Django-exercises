from django.urls import path, include
from rest_framework import routers

from api.views import (
    BookViewset,
    AuthorViewset,
    CreateManyBook,
    BookTitleView,
)

router = routers.SimpleRouter()
router.register(r"books", BookViewset)
router.register(r"authors", AuthorViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("create-many-books", CreateManyBook.as_view()),
    path("book-title/<pk>", BookTitleView.as_view()),
]
