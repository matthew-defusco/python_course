import smtplib
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

all_posts = requests.get('https://api.npoint.io/b400d972c38d5f2258b7').json()

@app.route('/')
def home():
  return render_template('index.html', posts=all_posts)

@app.route('/posts/<int:post_id>')
def post(post_id):
  single_post = requests.get(f'https://api.npoint.io/b400d972c38d5f2258b7/{post_id}').json()
  return render_template('post.html', post=single_post)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
  if request.method == 'GET':
    return render_template('contact.html', page_heading="Contact us!", page_subheading="Have questions? I have answers.")
  elif request.method == 'POST':
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
      connection.starttls()
      connection.login(
        user="dev.testing.5878@gmail.com",
        password="{{PUT PASSWORD HERE}}"
      )
      try:
        connection.sendmail(
          from_addr="dev.testing.5878@gmail.com",
          to_addrs="dev.testing5878@yahoo.com",
          msg=f"Subject: New message from contact form!\n\n{name} sent you a message.\n You can reach them at {email}.\n"
              f"Or call them at {phone}.\nHere's what they have to say: {message}"
        )
        return render_template('contact.html', page_heading="Message sent!", page_subheading="We'll respond soon 😘")
      except Exception as e:
        print(e)
      finally:
        connection.close()

# @app.route('/send', )
# def send():
#   name = request.form["name"]
#   email = request.form["email"]
#   phone = request.form["phone"]
#   message = request.form["message"]
#   return f'Name: {name}, email: {email}, phone: {phone}, message: {message}'
  # with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
  #   connection.starttls()
  #   connection.login(
  #     user="dev.testing.5878@gmail.com",
  #     password="chhtiosxcnzezios"
  #   )
  #   connection.sendmail(
  #     from_addr="dev.testing.5878@gmail.com",
  #     to_addrs="dev.testing5878@yahoo.com",
  #     msg=f"Subject: New message from contact form!\n\n{'replace'}"
  #   )
  #   connection.close()

if __name__ == '__main__':
  app.run(debug=True)
