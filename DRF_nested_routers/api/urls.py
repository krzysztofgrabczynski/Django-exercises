from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from api import views as api_views

router = routers.DefaultRouter()
router.register(r"authors", api_views.AuthorViewset, basename="authors")
router.register(r"books", api_views.BookViewset, basename="books")
router.register(r"libraries", api_views.LibraryViewset, basename="libraries")

libraries_router = nested_routers.NestedSimpleRouter(
    router, r"libraries", lookup="library"
)
libraries_router.register(
    r"books", api_views.BookViewset, basename="library-books"
)

books_router = nested_routers.NestedSimpleRouter(
    libraries_router, r"books", lookup="books"
)
books_router.register(
    r"authors", api_views.AuthorViewset, basename="library-book-authors"
)


urlpatterns = [
    path("", include(router.urls)),
    path("", include(libraries_router.urls)),
    path("", include(books_router.urls)),
]
