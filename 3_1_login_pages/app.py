"""
Basic login page Flask app.

Note that this version of the code is not even remotely secure - please DON'T plug in
real usernames and passwords! We'll make a secure version of this webpage in lesson
3.2.

Based on a tutorial from realpython.com:
    https://realpython.com/blog/python/introduction-to-flask-part-2-creating-a-login-page/
"""
__author__ = "Charlie Friend"


from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USERNAME = 'admin'
PASSWORD = 'nimda'


@app.route("/home")
def home():
    return "Welcome!"


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    # If we are POSTing to the /login route, then check the credentials!
    if request.method == "POST":
        requested_username = request.form['username']
        requested_password = request.form['password']

        if requested_username == USERNAME and requested_password == PASSWORD:
            print("Logged in!")
            return redirect("/home")
        else:
            error = "Incorrect username or password! Please try again!"
            print("Login failed!")

    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
