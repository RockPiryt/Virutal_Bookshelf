from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
    
with app.app_context():
    # db.create_all()

    # # --------------------------------Create records
    # first_book = Book(id=1, title="Pierwszaki z kosmosu", author="Rafał Witek", rating=6.5)
    # db.session.add(first_book)
    # second_book = Book(id=2, title="Potwór ekologiczny", author="Natalia Usenko", rating=7.3)
    # db.session.add(second_book)
    # db.session.commit()

    # # --------------------------------Read all records
    all_books = db.session.query(Book).all()
    # print(all_books)#print list  with title __repr__[<Book Pierwszaki z kosmosu>, <Book Potwór ekologiczny>]
    for book in all_books:
        print(f"Name =  {book.title}")
        print(f"Author =  {book.author}")
        print(f"Rating =  {book.rating}\n")
    
    # #  -----------------------------Read a specific record by title
    selected_book = Book.query.filter_by(title="Pierwszaki z kosmosu").first()
    # print(selected_book.title)
    # print(selected_book.rating)

    # # ----------------------------------------Read a specific record by id
    selected_book = Book.query.filter_by(id=1).first()
    # print(selected_book.title)

    # # ------------------------------Update a Particular record
    # book_to_update = Book.query.filter_by(title="Pierwszaki z kosmosu").first()
    # book_to_update.title = "Pierwszaki z kosmosu to lektura"
    # db.session.commit() 

    # #--------------------------------Select Using Primary Key
    # book_id = 1
    # book_to_update = Book.query.get(book_id)
    # book_to_update.title = "Pierwszaki z kosmosu to lektura dla gimbazy"
    # db.session.commit()

    # #--------------------------------Delete Using Primary Key
    book_id = 1
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()



if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)