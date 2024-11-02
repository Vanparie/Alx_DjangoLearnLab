# Update Operation
### Command:
```python
Book = Book.objects.get(id=1)
Book.title = "Nineteen Eighty-Four"
Book.save()
Book  # Display updated instance

# Expected output

<Book: Nineteen Eighty-Four by George Orwell>
