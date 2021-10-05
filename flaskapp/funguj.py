from flask import Flask, render_template, request, flash, redirect, url_for  # import flask
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from datetime import date
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test")
def kuk_templejt():
    return render_template("kuk.html",today=str(date.today()))

if  __name__=="__main__":
    app.run()



class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
            flash('Thanks for registering')
            return redirect(url_for('login'))
        return render_template('test.html', form=form)