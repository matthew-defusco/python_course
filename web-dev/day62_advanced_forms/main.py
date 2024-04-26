from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[InputRequired()])
    location_url = StringField('Location URL', validators=[InputRequired(), URL()])
    open_time = StringField('Open Time', validators=[InputRequired()])
    close_time = StringField('Close Time', validators=[InputRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=["☕️","☕️☕️","☕️☕️☕️","☕️☕️☕️☕️","☕️☕️☕️☕️☕️"])
    wifi_rating = SelectField('WiFi Rating', choices=["𝕏", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    power_rating = SelectField('Power Rating', choices=["🔌","🔌🔌","🔌🔌🔌"])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        row = [form.cafe.data, form.location_url.data, form.open_time.data, form.close_time.data,
               form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data]
        with open('cafe-data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
        return redirect('/')
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
