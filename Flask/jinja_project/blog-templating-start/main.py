from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

@app.route('/')
def home():
    post_data = Post()
    data = post_data.data
    return render_template("index.html", data=data)

@app.route('/post/<int:num>')
def get_post(num):
    post_data = Post()
    content = post_data.return_content(num)
    return render_template("post.html", text = content['body'], title=content['title'])

if __name__ == "__main__":
    app.run(debug=True)
