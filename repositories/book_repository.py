from db.run_sql import run_sql
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        book = Book(result['title'], result['genre'], result['author'], result['id'])
    return book

def save(book):
    sql = "INSERT INTO books (title, genre, author_id) VALUES ( ?, ?, ?) RETURNING *"
    values = [book.title, book.genre, book.author.id]
    results = run_sql(sql, values)
    # this line takes the first value returned 0 and drills down to the id
    id = results[0]['id']
    # what does this part do????????
    book.id = id
    return book

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def update(book):
    sql = "UPDATE books SET (title, genre, author) = ( ?, ?, ?) WHERE id = ?"
    values = [book.title, book.genre, book.author.id, book.id]
    run_sql(sql, values)
