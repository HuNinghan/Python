from flask import flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/bye')
def bye():
    return 'Bye'


if __name == "__main__":
    app.run()
