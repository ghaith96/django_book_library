from django.urls import path
from .views import BooksListView

app_name = "books"

urlpatterns = [
    path("", BooksListView.as_view(), name="home"),
]
