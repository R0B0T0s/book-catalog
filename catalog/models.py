from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    body = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review of {self.book.title}"