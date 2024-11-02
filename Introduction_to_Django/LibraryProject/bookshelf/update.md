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
