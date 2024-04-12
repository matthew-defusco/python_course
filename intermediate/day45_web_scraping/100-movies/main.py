import os
import requests
from bs4 import BeautifulSoup
import lxml

script_dir = os.path.dirname(os.path.relpath(__file__))

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "lxml")

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
# movie_titles.reverse()
movies = movie_titles[::-1]

with open(f"{script_dir}/movies.txt", mode="w+") as file:
  for movie in movies:
    file.writelines(movie + "\n")