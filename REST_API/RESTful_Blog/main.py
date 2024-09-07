from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>",methods=['GET'])
def show_post(index):
    requested_post = BlogPost.query.get(index)
    return render_template("post.html", post=requested_post)

@app.route("/new-post",methods=['POST','GET'])
def new_post():
    options='new_post'
    input_form = CreatePostForm()
    if input_form.validate_on_submit():
        # today = datetime.today().strftime('%m-%d-%Y').split('-')
        # month = calendar.month_name[int(today[0])]
        # today_date = f'{month} {today[1]}, {today[2]}'
        new_post = BlogPost(
            title = input_form.title.data,
            subtitle = input_form.subtitle.data,
            date = date.today().strftime("%B %d, %Y"),
            body = input_form.body.data,
            author = input_form.author.data,
            img_url = input_form.img_url.data,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html',form=input_form,type_of=options)

@app.route('/edit-post/<int:post_id>',methods=['GET','POST','PATCH'])
def edit_post(post_id):
    options='edit_post'
    original_form = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=original_form.title,
        subtitle = original_form.subtitle,
        body=original_form.body,
        author = original_form.author,
        img_url = original_form.img_url
    )
    if edit_form.validate_on_submit():
        original_form.title = edit_form.title.data
        original_form.subtitle = edit_form.subtitle.data
        original_form.author = edit_form.author.data
        original_form.img_url = edit_form.img_url.data
        original_form.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html',type_of = options,form=edit_form)

@app.route('/delete/<int:post_id>', methods=['GET','DELETE'])
def delete(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session().delete(post_to_delete)
    db.session().commit()
    return redirect(url_for('get_all_posts'))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)