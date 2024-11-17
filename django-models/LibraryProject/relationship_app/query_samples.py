import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
import django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author():
    author_name = 'Author Name'  # Replace with the author's name
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    print(f'Books by {author_name}:')
    for book in books:
        print(book.title)

# List all books in a library
def books_in_library():
    library_name = 'Library Name'  # Replace with the library's name
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f'Books in {library_name}:')
    for book in books:
        print(book.title)

# Retrieve the librarian for a library
def librarian_for_library():
    library_name = 'Library Name'  # Replace with the library's name
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f'Librarian for {library_name}: {librarian.name}')

if __name__ == '_main_':
    books_by_author()
    books_in_library()
    librarian_for_library()