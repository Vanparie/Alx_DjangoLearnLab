# Create Operation
### Command:
```python
from bookshelf.models import Book
Book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
Book  # Display the book instance

# Expected output
<Book: 1984 by George Orwell>

# Update Operation
### Command:
```python
Book = Book.objects.get(id=1)
Book.title = "Nineteen Eighty-Four"
Book.save()
Book  # Display updated instance

# Expected output
<Book: Nineteen Eighty-Four by George Orwell>

# Retrieve Operation
### Command:
```python
Book.objects.all()

# Expected output
<QuerySet [<Book: 1984 by George Orwell>]>

# Delete Operation
### Command:
```python
book.delete()
Book.objects.all()

# Expected output
(1, {'bookshelf.Book': 1})
<QuerySet []>