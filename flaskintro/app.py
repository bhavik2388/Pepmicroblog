# python -m venv .venv
# source .venv/Scripts/activate
# pip install Flask
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run

from flask import Flask, render_template
from jinja2 import Template
#flask class from flask package

app = Flask(__name__) #dunder name, always unique

class Planets:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/expressions/")
def expressions():

    #interpolation
    name="Steve"
    language_name = "Jinja2"

    #Addition, subtraction
    no_of_oranges=5
    no_of_apples=7
    old_quantity=9
    new_quantity=4
    first_name="Tony"
    last_name = "Stark"


    # return render_template("jinja_intro.html",
    #                         name=name,
    #                         language_name=language_name,
    #                         no_of_oranges=no_of_oranges,
    #                         no_of_apples=no_of_apples,
    #                         old_quantity=old_quantity,
    #                         new_quantity=new_quantity,
    #                         first_name=first_name,
    #                         last_name=last_name)

    kwargs = {
        "name":name,
        "language_name":language_name,
        "no_of_oranges":no_of_oranges,
        "no_of_apples":no_of_apples,
        "old_quantity":old_quantity,
        "new_quantity":new_quantity,
        "first_name":first_name,
        "last_name":last_name
    }

    return render_template("jinja_intro.html", **kwargs)

@app.route('/data-structures/')
def render_data_structures():
    movies=[
        "Shawshank Redemption",
        "Spider-man: No way home",
        "Avengers: Endgame"
    ]

    car={
        "brand":"Nissan",
        "model":"President",
        "year":"1992"
    }

    planets = Planets("Mercury", "Venus", "Earth","Mars")
    # return render_template("data_structures.html", movies=movies, car=car, planets=planets)

    kwargs={
        "movies":movies,
        "car":car,
        "planets":planets
    }
    return render_template("data_structures.html", **kwargs)

@app.route('/conditionals-basics/')
def render_conditionals():
    course = "Backend"
    company = ""
    return render_template("conditionals.html", course = course, company=company)

@app.route('/for-loop/')
def render_loops_for():
    planets=[
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]
    return render_template("for_loop.html", planets=planets)

@app.route('/for-loop/conditionals/')
def render_for_loops_conditionals():
    department_os = {
        "Frontend": "MacOS",
        "Backend": "Linux",
        "Database": "Windows"
    }

    return render_template("loops_and_conditionals.html", department_os=department_os)