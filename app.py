from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.secret_key = "qantas_demo"
@app.route("/login/<username>")
def login(username):
    session["user"] = username
    return redirect(url_for("dashboard"))
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)
