import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')  # Update if project name is different
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. All books by a specific author
    author_name = "George Orwell"
    books = Book.objects.filter(author__name=author_name)
    print(f"Books by {author_name}:")
    for book in books:
        print(f" - {book.title}")

    # 2. All books in a specific library
    library_name = "Main Branch"
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in {library.name}:")
        for book in library.books.all():
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

    # 3. Librarian for a specific library
    try:
        librarian = Librarian.objects.get(library__name=library_name)
        print(f"\nLibrarian of {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for '{library_name}'.")

if __name__ == "__main__":
    run_queries()
