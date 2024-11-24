# api/urls.py
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Register the ViewSet

urlpatterns = [
    # Existing endpoint for the BookList view (if you still want to keep it)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router-generated URLs
    path('', include(router.urls)),  # This automatically generates URLs for CRUD operations
]