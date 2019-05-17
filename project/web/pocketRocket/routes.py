from pocketRocket import app
from flask import render_template, request, redirect, flash, url_for, Markup
from werkzeug.urls import url_parse
import os


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    return render_template("index.html")