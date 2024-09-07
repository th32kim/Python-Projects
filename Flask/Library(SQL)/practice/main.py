from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pyparsing import null_debug_action


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250),unique=True, nullable = False)
    author = db.Column(db.String(250), nullable = False)
    rating = db.Column(db.Float,nullable = False)

    def __repr__(self):
        return '<title %r>' % self.title

# db.create_all()
# first_book = Post(title='Harry Potter', author = 'J.K Rowling', rating=9.3)
# db.session.add(first_book)
# book_to_update = Post.query.filter_by(title='Harry Potter').first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()
# db=sqlite3.connect("Flask/Library(SQL)/practice/books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (\
# #     id INTEGER PRIMARY KEY, \
# #     title varchar(250) NOT NULL UNIQUE, \
# #     author varchar(250) NOT NULL, \
# #     rating FLOAT NOT NULL)")
all_books = db.session.query(Post).all()
print(all_books)
# cursor.execute("INSERT INTO books \
# VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()