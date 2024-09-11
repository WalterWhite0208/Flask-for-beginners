from flask import Flask
app = Flask(__name__)


# Static Routes
@app.route('/')
def home():
    return "Welcome to home page"

@app.route('/about')
def about():
    return "This is a About page"

# Dynamic Routes
@app.route('/user/<name>')
def greet(name):
    return f"Hello, {name}"

@app.route('/blog/<int:post_id>')
def show_post(post_id):
    return f"This is a blog post {post_id}"

# URL Converters
@app.route('/score/<int:marks>')
def show_score(marks):
    return f"Your score is {marks}"

@app.route('/price/<float:amount>')
def show_price(amount):
    return f"The price is {amount}"


if __name__ == "__main__":
    app.run(debug=True)