from django.views.generic import ListView

from .models import Book

class BooksListView(ListView):
    model = Book
