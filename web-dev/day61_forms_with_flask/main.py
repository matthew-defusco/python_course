from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
app.secret_key = 'secret keys are good to use'

bootstrap = Bootstrap4(app)

class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[InputRequired(), Email()])
    password = PasswordField(label='Password', validators=[InputRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if (email == 'admin@email.com' and password == '12345678'):
            return redirect('success')
        else:
            return redirect('denied')
    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
