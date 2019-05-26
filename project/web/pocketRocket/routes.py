from pocketRocket import app
from flask import render_template, request, redirect, flash, url_for, Markup
from werkzeug.urls import url_parse
from pocketRocket.forms import rootAlgorithms
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from pocketRocket.methods.bincremental import busqueda_incremental
from pocketRocket.methods.biseccion import biseccion
from pocketRocket.methods.regla_falsa import regla_falsa
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


@app.route('/falsePosition', methods=['GET', 'POST'])
def false_position():
    form = rootAlgorithms()
    if request.method == 'POST':
        f_x = form.function.data
        x_0 = form.x_0.data
        x_1 = form.x_1.data
        n = form.n_max.data
        tol = form.tol.data
        x = symbols('x', real=True)
        parser = parse_expr(f_x, locals())
        result = regla_falsa(parser, x_0, x_1, tol, n)
        form.result.data = result
    return render_template("false_position.html", form=form)


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

@app.route('/gaussTotalPivot')
def gauss_totalpivot():
    return render_template("gauss_totalpivot.html")


@app.route('/gaussPartialPivot')
def gauss_partialpivot():
    return render_template("gauss_partialpivot.html")


@app.route('/luSimpleGaussian')
def lu_simple_gaussian():
    return render_template("lu_simple_gaussian.html")


@app.route('/pa')
def pa():
    return render_template("pa_factorization.html")


@app.route('/luPivoting')
def lu_pivoting():
    return render_template("lu_pivoting.html")


@app.route('/crout')
def crout():
    return render_template("crout.html")


@app.route('/doolittle')
def doolittle():
    return render_template("doolittle.html")


@app.route('/cholesky')
def lucholeskypivoting():
    return render_template("cholesky.html")

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
