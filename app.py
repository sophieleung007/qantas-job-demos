from flask import Flask, render_template, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "qantas_demo")

@app.route("/")
def home():
    return redirect(url_for("login", username="guest"))  # Redirect with default username

@app.route("/login/<username>")
def login(username):
    session["user"] = username
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect(url_for("login", username="guest"))  # Fallback redirect

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=False)