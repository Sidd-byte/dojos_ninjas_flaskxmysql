from flask import render_template, redirect
from dojos_ninjas_app import app
from dojos_ninjas_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)