from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
import sqlalchemy
from wtforms import StringField, SubmitField,validators,FloatField,IntegerField,URLField
from wtforms.validators import DataRequired
import requests
import sqlalchemy_utils


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Database Structure
class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80),unique=True, nullable=False)
    year = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(250),nullable=False)
    rating = db.Column(db.Float,nullable=True)
    ranking = db.Column(db.Integer,nullable=True)
    review = db.Column(db.String(250),nullable=True)
    img_url = db.Column(db.String(250),unique=True, nullable=False)

#Creating new database - needs to be outside of the database structure!!!
if not sqlalchemy_utils.functions.database_exists("sqlite:///movies.db"):
    db.create_all()

#form for new movies
class AddMovieForm(FlaskForm):
    title = StringField(label='Title of the Movie',validators=[DataRequired(message="You can not leave this field empty")])
    submit = SubmitField(label="Add Movie")

class RateMovieForm(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 7.5")
    review = StringField(label="Your Review")
    submit = SubmitField(label="Done")

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies)-i
    db.session.commit()
    return render_template("index.html",movies=all_movies)

#Editing new movies
@app.route('/edit',methods=['GET','POST'])
def edit():
    edit_form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    if edit_form.validate_on_submit():
        movie.rating = edit_form.rating.data
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html',form=edit_form,movie = movie)

API_KEY="d8f3fcce2702229a56caeddc9b191896"
API_URL="https://api.themoviedb.org/3/search/movie?"
#Adding new movies
@app.route('/add',methods=['GET','POST'])
def add():
    add_form = AddMovieForm()

    if add_form.validate_on_submit():
        movie_add = add_form.title.data
        response = requests.get(API_URL, params={'api_key': API_KEY, 'query': movie_add})
        movie_options = response.json()['results']
        return render_template('select.html',options = movie_options)
    return render_template('add.html',form=add_form)

MOVIE_DETAIL_API = "https://api.themoviedb.org/3/movie/"
IMAGE_URL='https://image.tmdb.org/t/p/w500'
#finding movies according to the api
@app.route('/find_movie',methods=['GET','POST'])
def find_movie():
    movie_id = request.args.get('id')
    if movie_id:
        response = requests.get(url=f'{MOVIE_DETAIL_API}/{movie_id}',params={'api_key':API_KEY,'language':'en-US'})
        data = response.json()
        new_movie = Movie(
            title=data['original_title'],
            year=data['release_date'].split("-")[0],
            description=data['overview'],
            rating=data['vote_average'],
            review='please edit this field',
            ranking='0',
            img_url = f"{IMAGE_URL}{data['backdrop_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit',id=new_movie.id))

#Deleting Movie
@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session().delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
