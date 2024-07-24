# Import Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)


# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, Flask!'


# Check if the executed file is the main program
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
