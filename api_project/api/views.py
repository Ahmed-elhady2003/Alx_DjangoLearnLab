from django.shortcuts import render
# api/views.py
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the serializer to format data
# Create your views here.
generics.ListAPIView