import pdb
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("J D Salinger")
# resave author1 above with the newly save database version icluding id
author_repository.save(author1)
author2 = Author("Philip K Dick")
author_repository.save(author2)
author3 = Author("Steven King")
author_repository.save(author3)
author4 = Author("Alan Moore")
author_repository.save(author4)
author5 = Author("Patricia Highsmith")
author_repository.save(author5)

book1 = Book("The Minority Report", "Science Fiction", author2)
book_repository.save(book1)
book2 = Book("The Man in the High Castle", "Alternative History", author2)
book_repository.save(book2)
book3 = Book("Watchmen", "Science Fiction", author4)
book_repository.save(book3)
book4 = Book("From Hell", "Science Fiction", author4)
book_repository.save(book4)
book5 = Book("V for Vendetta", "Science Fiction", author4)
book_repository.save(book5)
book6 = Book("Strangers on a Train", "Fiction", author5)
book_repository.save(book6)
book7 = Book("The Talented Mr Ripley", "Crime Fiction", author5)
book_repository.save(book7)

# The Book Ids seem to be sgtck at None. The authors are ok though?! 

book_repository.delete(book5.id)

for author in author_repository.select_all():
    print(author.__dict__)

for book in book_repository.select_all():
    print(book.__dict__)

pdb.set_trace()