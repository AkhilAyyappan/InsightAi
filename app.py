from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("students.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

if __name__ == "__main__":
    app.run(debug=True)
