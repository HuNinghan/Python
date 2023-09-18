from flask import flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/bye')
def bye():
    return 'Bye!'


@app.route('/username/<name>/<int:number>')
def greet(name):
    return f"Hi {name}, you are {number} years old."


if __name__ == "__main__":

    # debug mode allows saved changes to reflect immediately on server by refreshing
    app.run(debug=True)

    # app.run()
