import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
#    new_year = True
##    other way to put in python code
##    text = "Yes" if new_year else "NO" and then pass in the text
    return render_template("index.html", new_year=new_year)
