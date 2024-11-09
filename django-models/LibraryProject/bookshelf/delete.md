# Delete Operation
### Command:
```python

from bookshelf.models import Book
book.delete()
Book.objects.all()

# Expected output

(1, {'bookshelf.Book': 1})
<QuerySet []>
