from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive_data():
    user_name = request.form['name']
    user_pass = request.form['password']
    return f"<h1> Name: {user_name} Password: {user_pass}</h1>"

if __name__ == '__main__':
    app.run(debug=True)