# Create Operation
### Command:
```python
from bookshelf.models import Book
Book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
Book  # Display the book instance

# Expected output
<Book: 1984 by George Orwell>

# Update Operation

To update the title of a specific `Book` instance, retrieve it using `Book.objects.get()` and then modify the `title` attribute. Save the instance afterward to apply the change.

### Command:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)  # Replace `1` with the ID of the book you want to update
book.title = "Nineteen Eighty-Four"  # Update the title
book.save()  # Save the changes


# Expected output

<Book: Nineteen Eighty-Four by George Orwell>


# Retrieve Operation
To retrieve a specific `Book` instance by its ID, use the `Book.objects.get()` method.

### Command:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)  # Replace `1` with the ID of the book you want to retrieve
book

# Expected output
<QuerySet [<Book: 1984 by George Orwell>]>

# Delete Operation
### Command:
```python

from bookshelf.models import Book
book.delete()
Book.objects.all()

# Expected output
(1, {'bookshelf.Book': 1})
<QuerySet []>