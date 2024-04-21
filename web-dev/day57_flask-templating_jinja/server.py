import random
from datetime import datetime
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
  current_year = datetime.now().year
  random_number = random.randint(1, 10)
  return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
  age_response = requests.get(f'https://api.agify.io?name={name}').json()
  gender_response = requests.get(f'https://api.genderize.io?name={name}').json()
  # print(age_response.json())
  return render_template('age-gender.html', name=name, age=age_response['age'], gender=gender_response['gender'])


@app.route('/blog/<num>')
def get_blog(num):
  print(num)
  blog_url = "https://api.npoint.io/b0d671e1c3e0292da33b"
  response = requests.get(blog_url)
  all_posts = response.json()
  return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
  app.run(debug=True)
