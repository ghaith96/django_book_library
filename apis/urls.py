from django.urls import path
from .views import BookAPIView

app_name = "apis"

urlpatterns = [
    path("", BookAPIView.as_view(), name="book_list"),
]
