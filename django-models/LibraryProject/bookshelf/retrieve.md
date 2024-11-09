# Retrieve Operation

To retrieve a specific `Book` instance by its ID, use the `Book.objects.get()` method.

### Command:
```python
from bookshelf.models import Book
Book = Book.objects.get(id=1)  # Replace `1` with the ID of the book you want to retrieve
Book

# Expected output

<QuerySet [<Book: 1984 by George Orwell>]>
