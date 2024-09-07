from flask import Flask, render_template, request
import requests
API_URL = 'https://api.npoint.io/a14a50aa1385a1ecfbba'
post_response = requests.get(API_URL).json()
print(post_response)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', posts = post_response)

@app.route('/home')
def return_home():
    return render_template('index.html', posts = post_response)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/form-entry', methods=['POST'])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    message = request.form['message']

    print(name)
    print(email)
    print(phone_number)
    print(message)
    
    return 'Successfully submitted!'

if __name__ == '__main__':
    app.run(debug=True)