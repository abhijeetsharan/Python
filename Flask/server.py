from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["username"]
    return f"Hello, {name}!"

# Flask with json api
@app.route("/api")
def api():
    data = {"message": "Hello, Flask API!", "status": "success"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
