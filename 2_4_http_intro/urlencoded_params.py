"""
Basic Flask web server.
Run this program to start the web server, press CTRL+C to stop.
"""
__author__ = "Charlie Friend"

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    name = request.args.get("name")
    return "Hello " + name + "!"


@app.route('/hello')
def hello():
    return render_template("hello.html")


# Only run the app if this is the script being run. Otherwise importing this
# file will start the web server.
#
# Using host='0.0.0.0' causes the app to listen on all interfaces, so you
# should be able to access it from other computers on the local network.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
