from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import select

from models import db, Book

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-project-collection.db"
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    book_count = db.session.query(Book).count()
    all_books = db.session.execute(select(Book).order_by(Book.title)).scalars()
    return render_template('index.html', books=all_books, count=book_count)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        try:
            new_book = Book(
                title=request.form["title"],
                author=request.form["author"],
                rating=request.form["rating"]
            )
            db.session.add(new_book)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print("Something went wrong getting that saved to the db.")
            print(e)
    return render_template('add.html')

@app.route('/edit', methods=["GET", "POST"])
def edit():
    id = request.args.get('id')
    book_to_edit = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    if request.method == "GET":
        return render_template('edit.html', book=book_to_edit)
    elif request.method == "POST":
        try:
            book_to_edit.rating = request.form["rating"]
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print("Something went wrong updating")
            print(e)
            return redirect('/')

@app.route('/delete', methods=["POST"])
def delete():
    id = request.json["id"]
    book_to_delete = db.session.execute(select(Book).where(Book.id == id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

