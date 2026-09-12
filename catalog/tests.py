from django.test import TestCase
from django.urls import reverse
from .models import Publisher, Book

# Create your tests here.
class BookListTests(TestCase):
    def test_book_appears_on_books_page(self):

        publisher = Publisher.objects.create(name="Test Publisher")
        book = Book.objects.create(
            title="Unique Test Book Title 12345",
            pages=999,
            publisher=publisher
        )


        response = self.client.get(reverse("book_list"))


        self.assertContains(response, "Unique Test Book Title 12345")