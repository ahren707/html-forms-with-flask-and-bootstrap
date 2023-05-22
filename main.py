from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
Bootstrap(app)

class MyForm(FlaskForm):
    email = StringField(label='Email: ', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password: ', validators=[DataRequired(), Length(min=8, max=20, message="password must be 8-20 characters")])
    submit = SubmitField(label='Login')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    form = MyForm()
    form.validate_on_submit()
    if form.validate_on_submit() == True:
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)