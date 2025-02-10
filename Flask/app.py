from flask import Flask, render_template

app = Flask(__name__)  # Create Flask app instance

@app.route("/")  # Define route for home page
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "This is the About Page"

@app.route("/contact")
def contact():
    return "Contact us at contact@example.com"

@app.route("/homepage")
def homepage():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)  # Run the app
