from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold_function():
        return "<b>"+function()+"</b>"
    return bold_function

def make_emphasis(function):
    def emphasis():
        return "<em>"+function()+"</em>"
    return emphasis

def make_underlined(function):
    def underlined():
        return "<u>" + function() + "</u>"
    return underlined

@app.route('/bye')
@make_bold
def bye():
    return "bye"


# @app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>"\
        "<p>Thia is a pagagraph</p>"\
            "<img src='https://giphy.com/clips/bestfriends-best-friends-adopt-animal-adoption-cwQCUhKible5mGrtMO' width=200>"


@app.route('/username/<name>')
def greet(name):
    return f'hello{name}'


if __name__ == "__main__":
    app.run(debug=True)