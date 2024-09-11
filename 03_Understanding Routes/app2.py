from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "This is the home page"

@app.route('/user/<name>')
def greet(name):
    return f" Hello {name}, welcome to our website"

@app.route('/product/<int:id>')

def product(id):
    return f"This is product number {id}"

if __name__ == "__main__":
    app.run(debug=True)