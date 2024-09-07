from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home_route():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

random_number = random.randint(0,9)

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1>Too High</h1>"
    elif guess < random_number:
        return "<h1>Too low</h1>"
    else:
        return "<h1>Congratulation!!!!</h1>"

if __name__ == "__main__":
    app.run(debug=True)