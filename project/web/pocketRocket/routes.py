from pocketRocket import app
from flask import render_template, request, redirect, flash, url_for, Markup
from werkzeug.urls import url_parse
from pocketRocket.forms import rootAlgorithms
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from pocketRocket.methods.bincremental import busqueda_incremental
from pocketRocket.methods.biseccion import biseccion
import os

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("plotter.html")


@app.route('/grapher', methods=['GET', 'POST'])
def grapher():
    return render_template("plotter.html")


@app.route('/bisection', methods=['GET', 'POST'])
def bisection():
    form = rootAlgorithms()
    if request.method == 'POST':
        inter_a = form.inter_a.data
        inter_b = form.inter_b.data
        f_x = form.function.data
        n = form.n_max.data
        tol = form.tol.data
        x = symbols('x', real=True)
        parser = parse_expr(f_x, locals())
        result = biseccion(parser, inter_a, inter_b, n, tol)
        form.result.data = result
    return render_template("bisection.html", form=form)


@app.route('/incrementalSearch', methods=['GET', 'POST'])
def incremental_search():
    form = rootAlgorithms()
    if request.method == 'POST':
        f_x = form.function.data
        x_0 = form.x_0.data
        h = form.inter_h.data
        n = form.n_max.data
        tol = form.tol.data
        x = symbols('x', real=True)
        parser = parse_expr(f_x, locals())
        result = busqueda_incremental(parser, x_0, h, n, tol)
        form.result.data = result


    return render_template("incremental_search.html", form=form)


@app.route('/falsePosition')
def false_position():
    return render_template("false_position.html")


@app.route('/fixedPoint')
def fixed_point():
    return render_template("fixed_point.html")


@app.route('/secant')
def secant():
    return render_template("secant.html")


@app.route('/newton')
def newton():
    return render_template("newton.html")


@app.route('/multipleRoots')
def multiple_roots():
    return render_template("multiple_roots.html")


@app.route('/aitken')
def aitken():
    return render_template("aitken.html")


@app.route('/muller')
def muller():
    return render_template("muller.html")


@app.route('/steffenson')
def steffenson():
    return render_template("steffenson.html")


@app.route('/gaussSimple')
def gauss_simple():
    return render_template("gauss_simple.html")


@app.route('/lu')
def lu_factorization():
    return render_template("lu_factorization.html")


@app.route('/pa')
def pa():
    return render_template("pa_factorization.html")


@app.route('/directFactorization')
def direct_factorization():
    return render_template("direct_factorization.html")


@app.route('/jacobi')
def jacobi():
    return render_template("jacobi.html")


@app.route('/gaussSeidel')
def gauss_seidel():
    return render_template("gauss_seidel.html")

@app.route('/sor')
def sor():
    return render_template("sor.html")


@app.route('/lagrange')
def lagrange():
    return render_template("lagrange.html")


@app.route('/newtonPoly')
def newton_interpolation():
    return render_template("newton_interpolation.html")


@app.route('/vandermorde')
def vandermorde():
    return render_template("vandermorde.html")


@app.route('/splines')
def splines():
    return render_template("splines.html")