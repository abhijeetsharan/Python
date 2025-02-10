from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store tasks in a list
tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")  # Get task from form
    if task:
        tasks.append(task)  # Add task to list
    return redirect(url_for("home"))

@app.route("/delete/<int:index>")
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)  # Remove task by index
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
