from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


#To keep information from form
all_books = []


@app.route('/')
def home():
    return render_template("index.html", html_all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method =="POST":
        ##### Create dict
        f_title = request.form["title"]
        f_author = request.form["author"]
        f_rating = request.form["rating"]

        book = {
            "title": f_title,
            "author": f_author,
            "rating": f_rating,
        }

        all_books.append(book)

        # #######Dict comprehension
        # form_data = request.form
        # # print(form_data)#ImmutableMultiDict([('title', 'Alicja'), ('author', 'Górski'), ('rating', '3')])
        # new_dict={key:value for (key,value) in form_data.items()}
        # # print(new_dict)# {'title': 'Alicja', 'author': 'Górski', 'rating': '3'}
        # all_books.append(new_dict)

        # ##### to_dict method
        # all_books.append(request.form.to_dict())
        

        return redirect(url_for('home'))
    return render_template("add.html")
    



if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")

