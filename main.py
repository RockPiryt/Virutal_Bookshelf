from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push() 


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", html_all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method =="POST":

        ##### Create dict
        f_title = request.form["title"]
        f_author = request.form["author"]
        f_rating = request.form["rating"]

        added_book = Book(title=f_title, author=f_author, rating=f_rating)
        db.session.add(added_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template("add.html")
    

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_rating(book_id):
    edit_book = Book.query.filter_by(id=book_id).first()
    if request.method =="POST":
        edit_book.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit_page.html", html_book=edit_book)


# @app.route('/edit', methods=['GET', 'POST'])
# def edit_rating():
#     book_id_request = request.args.get('book_id')
#     edit_book = Book.query.filter_by(id=book_id_request).first()
#     if request.method =="POST":
#         edit_book.rating = request.form["new_rating"]
#         db.session.commit()
#         return redirect(url_for('home'))
#     return render_template("edit_page.html", html_book=edit_book)

@app.route('/delete/<int:book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    book_to_delete = Book.query.filter_by(id=book_id).first()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)