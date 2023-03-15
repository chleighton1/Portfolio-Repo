from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/octopus")
def octopus():
    return render_template("octopus.html")
