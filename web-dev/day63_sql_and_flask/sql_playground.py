from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float
import sqlite3

## Creating a DB with SQLAlchemy and Flask
# Set up the base class for creating tables, etc.
class Base(DeclarativeBase):
  pass

# Create an instance of SQLAlchemy class with the Base configuration
db = SQLAlchemy(model_class=Base)

# Create Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Connect SQLAlchemy to Flask app
db.init_app(app)

# Create a Book table class with the schema
class Book(db.Model):
  id: Mapped[int] = mapped_column(Integer, nullable=False, primary_key=True)
  title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
  author: Mapped[str] = mapped_column(String(250), nullable=False)
  rating: Mapped[float] = mapped_column(Float, nullable=False)

# Create the table
with app.app_context():
  db.create_all()

  book = Book(
    title = "Harry Potter",
    author = "J.K. Rowling",
    rating = 9.3
  )

  db.session.add(book)
  db.session.commit()

# if __name__ == "__main__":
#   app.run()

## Creating a DB from scratch
# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()

# cursor.execute('CREATE TABLE books (id INTEGER PRIMARY KEY,' \
#                'title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)')
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()