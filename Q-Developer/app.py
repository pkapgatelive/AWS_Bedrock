import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE) as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)


@app.route("/")
def index():
    tasks = sorted(load_tasks(), key=lambda t: t["priority"])
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name", "").strip()
    try:
        priority = int(request.form.get("priority", 0))
        if not name or not 1 <= priority <= 5:
            raise ValueError
    except ValueError:
        return redirect(url_for("index"))
    tasks = load_tasks()
    tasks.append({"name": name, "priority": priority})
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/remove/<int:index>", methods=["POST"])
def remove(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
