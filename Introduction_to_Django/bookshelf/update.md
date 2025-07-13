```python
from bookshelf.models import Book

# 1. Get the book to update
book = Book.objects.get(title="1984")

# 2. Update the title
book.title = "Nineteen Eighty-Four"

# 3. Save changes
book.save()

# Verify update
updated_book = Book.objects.get(id=book.id)
print(f"Updated Title: {updated_book.title}")
```

Expected Output:
```
Updated Title: Nineteen Eighty-Four
```
