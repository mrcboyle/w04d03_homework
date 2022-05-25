from db.run_sql import run_sql
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository

def select_all():
    authors = [] # create an empty list
    sql = "SELECT * FROM authors"
    results = run_sql(sql) # returns rows in sql format

    for row in results:
        author = Author(row['name'], row['id']) # convert to python format
        authors.append(author)
    return authors

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['name'], result['id'])
    return author

def save(author):
    sql = "INSERT INTO authors (name) VALUES (?) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    # what does this part do????????    
    author.id = id
    return author

def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM authors WHERE id = ?"
    values = [id]
    # if valueds = id (above) why dont' we just return id in thr run_sql below?
    run_sql(sql, values)

def update(author):
    sql = "UPDATE authors SET (name) = ( ?) WHERE id = ?"
    values = [author.name, author.id]
    run_sql(sql, values)
