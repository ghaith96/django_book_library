from django.urls import reverse
from django.test import TestCase

from .models import Book

class BookTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="good book title",
            subtitle="amazing book subtitle",
            author="the book author",
            isbn="1839562837",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "good book title")
        self.assertEqual(self.book.subtitle, "amazing book subtitle")
        self.assertEqual(self.book.author, "the book author")
        self.assertEqual(self.book.isbn, "1839562837")

    def test_book_listview(self):
        response = self.client.get(reverse("books:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "good book title")
        self.assertTemplateUsed("books/book_list.html")
