"""This is simulation of a web application using jinja 2 template to display my personal web page"""

#Imports
from flask import Flask, render_template, request,redirect,url_for

"""Instantiate flask as an app"""
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/templates/projects.html')
def projects():
    return render_template("projects.html")


if __name__ == '__main__':
    app.run()
