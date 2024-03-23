from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample user data (replace with your actual user database)
users = {
    "user1": {"username": "user1", "password": "password1"},
    "user2": {"username": "user2", "password": "password2"}
    "user3": {"username": "user3", "password": "password3"}
    "user4": {"username": "user4", "password": "password4"}
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        username = request.form["RajKumar"]
        password = request.form["password"]
        if username in users and users[username]["password"] == password:
            return redirect(url_for("dashboard", username=username))
        else:
            error = "Invalid username or password. Please try again."
            return render_template("login.html", error=error)
    return render_template("login.html")

@app.route("/dashboard/<username>")
def dashboard(username):
    return f"<h1>Welcome {username}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
