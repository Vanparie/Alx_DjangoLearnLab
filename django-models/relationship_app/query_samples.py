from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        
        return author.books.all()  # Using related_name from Book model
    except Author.DoesNotExist:
        return f"No author found with name: {author_name}"

def books_by_author(author):  
    try:
        author = Author.objects.filter(name=author)  
        return author.books.all()  # Using related_name from Book model
    except Author.DoesNotExist:
        return f"No author found with name: {author}"

# 2. List all books in a specific library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()  # Using related_name from Library model
    except Library.DoesNotExist:
        return f"No library found with name: {library_name}"

# 3. Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # Using related_name from Librarian model
    except Library.DoesNotExist:
        return f"No library found with name: {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to library: {library_name}"
