from pocketRocket import app
from flask import render_template, request, redirect, flash, url_for, Markup
from werkzeug.urls import url_parse
from pocketRocket.forms import rootAlgorithms, matrixAlgorithms, interpolationAlgorithms
from sympy import *
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from pocketRocket.methods.bincremental import busqueda_incremental
from pocketRocket.methods.biseccion import biseccion
from pocketRocket.methods.regla_falsa import regla_falsa
from pocketRocket.methods.puntoFijo import puntoFijo
from pocketRocket.methods.newton_raices_secante import secante, newton, multiple_roots
from pocketRocket.methods.factorizaciondirecta import crout_method, doolittle_method, cholesky
from pocketRocket.methods.sor import sor_method
from pocketRocket.methods.steffenson import steff
from pocketRocket.methods.vander_inter import vandermorde_method
from pocketRocket.methods.factorizacionlu import lu_simple_gauss
from pocketRocket.methods.factorizacionluparcial import lu_decomposition
from pocketRocket.methods.elimGaussSimple import eliminacion
from pocketRocket.methods.totalPivoting import totalPivoting
from pocketRocket.methods.elimGaussPivPar import gaussPivPar
from pocketRocket.methods.jacobi import jacobiClass
from pocketRocket.methods.seidel import seidelClass
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


@app.route('/fixedPoint', methods=['GET', 'POST'])
def fixed_point():
    form = rootAlgorithms()
    if request.method == 'POST':
        f_x = form.function.data
        g_x = form.function_g.data
        x_0 = form.x_0.data
        tol = form.tol.data
        n = form.tol.data
        x = symbols('x', real=True)
        parser_f = parse_expr(f_x, locals())
        parser_g = parse_expr(g_x, locals())
        result = puntoFijo(parser_f, parser_g, x_0, tol, n)
        form.result.data = result

    return render_template("fixed_point.html", form=form)


@app.route('/secant', methods=['GET', 'POST'])
def secant():
    form = rootAlgorithms()
    if request.method == 'POST':
        f_x = form.function.data
        x_0 = form.x_0.data
        x_1 = form.x_1.data
        tol = form.tol.data
        n = form.n_max.data
        x = symbols('x', real=True)
        parser = parse_expr(f_x, locals())
        result = secante(x_0, x_1, tol, n, parser)
        form.result.data = result

    return render_template("secant.html", form=form)


@app.route('/newton', methods=['GET', 'POST'])
def newton():
    form = rootAlgorithms()
    if request.method == 'POST':
        f_x = form.function.data
        f_x_derivate = form.first_derivate.data
        x_n = form.x_0.data
        tol = form.tol.data
        n = form.n_max.data
        x = symbols('x', real=True)
        parser_f = parse_expr(f_x, locals())
        parser_f_derivate = parse_expr(f_x_derivate, locals())
        result = newton(x_n, tol, n, f_x, f_x_derivate)
        form.result.data = result

    return render_template("newton.html", form=form)


@app.route('/multipleRoots', methods=['GET', 'POST'])
def multiple_roots():
    form = rootAlgorithms()
    if request.method == 'POST':
        f_x = form.function.data
        f_x_derivate = form.first_derivate.data
        f_x_derivate_2 = form.second_derivate.data
        x_n = form.x_0.data
        tol = form.tol.data
        x = symbols('x', real=True)
        parser_f = parse_expr(f_x, locals())
        parser_f_derivate = parse_expr(f_x_derivate, locals())
        parser_f_derivate_2 = parse_expr(f_x_derivate_2, locals())
        result = multipleRoots(x_n, tol, f_x, f_x_derivate, f_x_derivate_2)
        form.result.data = result

    return render_template("multiple_roots.html", form=form)


@app.route('/aitken')
def aitken():
    return render_template("aitken.html")


@app.route('/muller')
def muller():
    return render_template("muller.html")


@app.route('/steffenson', methods=['GET', 'POST'])
def steffenson():
    form = rootAlgorithms()
    if request.method == 'POST':
        f_x = form.function.data
        x_0 = form.x_0.data
        tol = form.tol.data
        n = form.n_max.data
        result = steff(f_x, x_0, tol, n)
        form.result.data = result

    return render_template("steffenson.html", form=form)


@app.route('/gaussSimple', methods=['GET', 'POST'])
def gauss_simple():
    form = matrixAlgorithms()
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        b_solution = form.b_solution.data.split(" ")
        result = eliminacion(matrix_a, b_solution)
        form.result.data = result

    return render_template("gauss_simple.html", form=form)


@app.route('/gaussTotalPivot', methods=['GET', 'POST'])
def gauss_totalpivot():
    form = matrixAlgorithms()
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        instance = totalPivoting(matrix_a)
        result = instance.elimination()
        form.result.data = result

    return render_template("gauss_totalpivot.html", form=form)


@app.route('/gaussPartialPivot', methods=['GET', 'POST'])
def gauss_partialpivot():
    form = matrixAlgorithms()
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        b_solution = form.b_solution.data.split(" ")
        result = gaussPivPar(matrix_a, b_solution)
        form.result.data = result

    return render_template("gauss_partialpivot.html", form=form)


@app.route('/luSimpleGaussian', methods=['GET', 'POST'])
def lu_simple_gaussian():
    form = matrixAlgorithms()
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        n = form.n_max.data
        result = lu_simple_gauss(matrix_a, int(n))
        form.result.data = result

    return render_template("lu_simple_gaussian.html", form=form)


@app.route('/luPivoting', methods=['GET', 'POST'])
def lu_pivoting():
    form = matrixAlgorithms()
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        result = lu_decomposition(matrix_a)
        form.result.data = result

    return render_template("lu_pivoting.html", form=form)


@app.route('/crout', methods=['GET', 'POST'])
def crout():
    form = matrixAlgorithms()
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        matrix_a = np.array(matrix_a)
        n = form.n_max.data
        result = crout_method(matrix_a, int(n))
        form.result.data = result

    return render_template("crout.html", form=form)


@app.route('/doolittle', methods=['GET', 'POST'])
def doolittle():
    form = matrixAlgorithms()
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        matrix_a = np.array(matrix_a)
        n = form.n_max.data
        result = doolittle_method(matrix_a, int(n))
        form.result.data = result

    return render_template("doolittle.html", form=form)


@app.route('/cholesky', methods=['GET', 'POST'])
def lucholeskypivoting():
    form = matrixAlgorithms()
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        matrix_a = np.array(matrix_a)
        n = form.n_max.data
        result = cholesky(matrix_a, int(n))
        form.result.data = result

    return render_template("cholesky.html", form=form)

@app.route('/jacobi', methods=['GET', 'POST'])
def jacobi():
    form = matrixAlgorithms()
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        x_0 = form.x_0.data.split(" ")
        n_max = form.n_max.data
        tol = form.tol.data
        instance = jacobiClass(n_max, tol, x_0, matrix_a)
        result = instance.jacobi_method()
        form.result.data = result

    return render_template("jacobi.html", form=form)


@app.route('/gaussSeidel', methods=['GET', 'POST'])
def gauss_seidel():
    form = matrixAlgorithms()
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        x_0 = form.x_0.data.split(" ")
        n_max = form.n_max.data
        tol = form.tol.data
        instance = seidelClass(n_max, tol, x_0, matrix_a)
        result = instance.gaussSeidel()
        form.result.data = result

    return render_template("gauss_seidel.html", form=form l)


@app.route('/sor', methods=['GET', 'POST'])
def sor():
    form = matrixAlgorithms()
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        matrix_a = np.array(matrix_a)
        b_solution = form.b_solution.data.split(" ")
        b_solution = [int(x) for x in b_solution]
        tol = form.tol.data
        w_sor = form.w_sor.data
        result = sor_method(matrix_a, b_solution, tol, w_sor)
        form.result.data = result

    return render_temb_solutionplate("sor.html", form=form)


@app.route('/lagrange')
def lagrange():
    return render_template("lagrange.html")


@app.route('/newtonPoly')
def newton_interpolation():
    return render_template("newton_interpolation.html")


@app.route('/vandermorde', methods=['GET', 'POST'])
def vandermorde():
    form = interpolationAlgorithms()
    if request.method == 'POST':
        x_points = form.x_points.data.split(" ")
        y_points = form.y_points.data.split(" ")
        result = vandermorde_method(x_points, y_points)
        form.result.data = result

    return render_template("vandermorde.html", form=form)


@app.route('/splines')
def splines():
    return render_template("splines.html")
