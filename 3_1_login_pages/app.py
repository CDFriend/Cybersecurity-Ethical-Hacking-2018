from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USERNAME = 'admin'
PASSWORD = 'nimda'


@app.route("/home")
def home():
    return "Welcome!"


@app.route("/login", methods=["GET", "POST"])
def login():

    # If we are POSTing to the /login route, then check the credentials!
    if request.method == "POST":
        requested_username = request.form['username']
        requested_password = request.form['password']

        if requested_username == USERNAME and requested_password == PASSWORD:
            print("Logged in!")
            return redirect("/home")
        else:
            print("Login failed!")

    return render_template('login.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
