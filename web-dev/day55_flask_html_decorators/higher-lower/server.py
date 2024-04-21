import random
from flask import Flask

app = Flask(__name__)

randum_number = random.randint(0, 9)

@app.route('/')
def root():
  return '<h1>Guess a number between 0 and 9</h1>' \
    '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXRiNHN6NWd3ejFtc2QwM2o2ZDc1Zm05ZmE4M2FubnYwc29zMTl0MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT5LMMneIRG1UJquOI/giphy.gif" />'

@app.route('/<int:number>')
def number_route(number):
  if number > randum_number:
    return '<h1 style="color: teal">Your guess is too high!</h1>' \
    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'
  elif number < randum_number:
    return '<h1 style="color: rebeccapurple">Too low!</h1>' \
    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'
  else:
    return '<h1 style="color: rebeccapurple">That\'s correct!!!!!!</h1>' \
    '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'



if __name__ == "__main__":
  app.run(debug=True)