warning: `VIRTUAL_ENV=C:\Users\ryand\OneDrive\Desktop\WT Coding Class\cidm3312\django-test\.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_book_appears_on_books_page (catalog.tests.BookListTests.test_book_appears_on_books_page)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\ryand\OneDrive\Desktop\WT Coding Class\cidm3312\book-catalog\catalog\tests.py", line 20, in test_book_appears_on_books_page
    self.assertContains(response, "Unique Test Book Title 12345")
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: False is not true : Couldn't find 'Unique Test Book Title 12345' in the following response
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <title>Book Catalog</title>\n</head>\n<body>\n    <nav>\n        <a href="/">Books</a> |\n        <a href="/publishers/">Publishers</a> |\n        <a href="/reviews/">Reviews</a>\n    </nav>\n    <hr>\n\n    \n    <h1>Books</h1>\n    <ul>\n        \n    </ul>\n\n</body>\n</html>'

----------------------------------------------------------------------
Ran 1 test in 0.020s

FAILED (failures=1)
Destroying test database for alias 'default'...

The failure message told me that the test correctly detected when "Books" stopped showing books form the database.

Q1- I put the ForeignKey on the Book model pointing to Publisher. I did this because each book belongs to one publisher, while a publisher can have many books. If I had reversed it, each publisher could only be linked to one book, having only one book is no good when running a publishing company.

Q2- I chose PositiveIntegerField for the page count because the number of pages is a whole number that can't be negative. If I had stored it as a CharField I would lose the ability to treat it as a real number. 