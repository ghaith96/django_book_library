from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book

class APITest(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="good book title",
            subtitle="amazing book subtitle",
            author="the book author",
            isbn="1839562837",
        )


    def test_api_listview(self):
        response = self.client.get(reverse("apis:book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.book)
