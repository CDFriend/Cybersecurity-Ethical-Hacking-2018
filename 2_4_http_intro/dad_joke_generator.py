"""
'Dad Joke Generator' Flask App

Step 1: Pick random dad joke
Step 2: Render to HTML
Step 3: Laugh
Step 4: Cry
"""

__author__ = "Charlie Friend"

import random
from flask import Flask, render_template

dad_jokes = [
    "Did you hear about the restaurant on the moon? Great food, no atmosphere.",
    "Want to hear a joke about paper? Nevermind it's tearable. ",
    "What do you call a fake noodle? An Impasta.",
    "What did the grape do when he got stepped on? He let out a little wine.",
    "5/4 of people admit that they’re bad with fractions.",
    "I thought about going on an all-almond diet. But that's just nuts"
]

app = Flask(__name__)


@app.route("/joke")
def joke():
    next_joke = random.choice(dad_jokes)
    return render_template("jokegenerator.html", joke=next_joke)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
