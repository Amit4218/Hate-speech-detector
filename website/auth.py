from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route('/')
def base():
    return render_template("base.html")

@auth.route('/mission')
def mission():
    return render_template("mission.html")

@auth.route('/Team')
def team():
    return render_template("team.html")
