<Book: Nineteen Eighty-Four by George Orwell (1949)>
#### In update.md
markdown
# Update Operation
Command:
python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book