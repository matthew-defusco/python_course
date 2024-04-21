from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    all_posts = requests.get("https://api.npoint.io/ef4d88e4d462158953cf").json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:post_id>')
def blog_post(post_id):
    blog_post = requests.get(f'https://api.npoint.io/ef4d88e4d462158953cf/{post_id}').json()
    return render_template("post.html", post=blog_post)

if __name__ == "__main__":
    app.run(debug=True)
