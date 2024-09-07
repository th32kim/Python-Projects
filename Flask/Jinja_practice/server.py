from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    this_year = date.today().year
    return render_template('index.html', num=random_number, year=this_year)

@app.route('/guess/<random_name>')
def guess(random_name):
    gender_url = f'https://api.genderize.io?name={random_name}'
    age_url = f'https://api.agify.io?name={random_name}'
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age_r = age_data['age']
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender_r = gender_data['gender']
    return render_template('index.html', name = random_name,age = age_r, gender = gender_r)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_data = requests.get(blog_url)
    data = blog_data.json()
    return render_template('blog.html', posts=data)

if __name__ == '__main__':
    app.run(debug=True)