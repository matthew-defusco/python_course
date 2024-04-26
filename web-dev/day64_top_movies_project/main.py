import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from sqlalchemy import select
import requests
from dotenv import load_dotenv

from db.my_database import db
from models.movie import Movie
from forms.edit import EditForm
from forms.find import FindForm

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

db.init_app(app)

with app.app_context():
    db.create_all()

Bootstrap5(app)


@app.route("/")
def home():
    # Get all the movies ordered by rating
    # db_movies = Movie.query.order_by(Movie.rating).all()
    all_movies = db.session.execute(select(Movie).order_by(Movie.rating)).scalars().all()
    # Update the ranking field for each of the movies
    ranking = len(all_movies)
    for movie in all_movies:
        movie.ranking = ranking
        ranking -= 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route('/find', methods=["GET", "POST"])
def find():
    find_form = FindForm()
    if request.method == "POST":
        headers = {
            "Authorization": f"Bearer {os.environ["TMDB_READ_TOKEN"]}"
        }
        movie_response = requests.get(f'https://api.themoviedb.org/3/search/movie?query={find_form.title.data}', headers=headers).json()
        movies = movie_response["results"]
        return render_template('select.html', movies=movies)
    return render_template('find.html', form=find_form)

@app.route('/add', methods=["GET", "POST"])
def add():
    movie_id = request.args.get('id')
    if movie_id:
        movie_to_add = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}', params={"api_key": os.environ["TMDB_API_KEY"], "language": "en-US"}).json()
        release_date=movie_to_add["release_date"].split("-")[0]
        # image = requests.get(f"https://image.tmdb.org/t/p/w780{movie_to_add["backdrop_path"]}")
        movie = Movie(
            title=movie_to_add["title"],
            year=release_date,
            description=movie_to_add["overview"],
            rating=movie_to_add["vote_average"],
            ranking=0,
            review="",
            img_url=f"https://image.tmdb.org/t/p/w780{movie_to_add["backdrop_path"]}"
        )
        db.session.add(movie)
        db.session.commit()
        return redirect(f'/edit/{movie.id}')

@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    movie_to_edit = db.get_or_404(Movie, id)
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        rating = edit_form.rating.data
        review = edit_form.review.data
        movie_to_edit.rating = rating
        movie_to_edit.review = review
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', form=edit_form)

@app.route('/delete/<int:id>')
def delete(id):
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
