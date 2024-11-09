# Create Operation
### Command:
```python
from bookshelf.models import Book
Book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
Book  # Display the book instance

# Expected output

<Book: 1984 by George Orwell>
