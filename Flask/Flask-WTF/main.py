from tokenize import String
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,validators
from flask_wtf.csrf import CSRFProtect
import os
from wtforms.validators import DataRequired
import email_validator
from flask_bootstrap import Bootstrap


csrf = CSRFProtect()

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)
Bootstrap(app)

class LoginForm(FlaskForm):
    Email= StringField(label='Email',validators=[validators.Email(message=(u'Invalid email address.'))])
    Password = PasswordField(label='Password', validators=[validators.Length(min=8,message=(u'Field must be at least 8 characters long'))])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    login_form=LoginForm()
    if login_form.validate_on_submit():
        if login_form.Email.data == 'admin@email.com' and login_form.Password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html',form=login_form)


if __name__ == '__main__':
    app.run(debug=True)