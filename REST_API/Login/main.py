from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
import werkzeug
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, email,password,name):
        self.email = email
        self.password = generate_password_hash(password, method='pbkdf2:sha256',salt_length=8)
        self.name = name

    
#flask login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=['POST','GET'])
def register():
    if request.method=='POST':
        user_name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        user = User.query.filter_by(email = email).first()
        if user:
            flash('The following email is already in use, login instead')
            return redirect(url_for('login'))
        if not user:
            new_user = User(email,password,user_name)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('secrets'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        email_input = request.form['email']
        password_input = request.form['password']
        user = User.query.filter_by(email = email_input).first()
        if not user:
            flash('Following account does not exist!')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password,password_input):
            flash('Password Incorrect!')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html",name = current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/download/<path:filename>',methods=['GET'])
def download(filename):
    return send_from_directory(directory='static/files', path=filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
