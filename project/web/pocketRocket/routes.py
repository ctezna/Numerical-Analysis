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
from pocketRocket.methods.newton_raices_secante import secante, newton_method, multiple_roots_method
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
from pocketRocket.methods.muller import muller_method
from pocketRocket.methods.lagrange_interpolacion import lagrange_method
from pocketRocket.methods.newton_interpolacion import newton_inter
from pocketRocket.methods.secante import secante_method
from pocketRocket.methods.spline1 import spline1_main
from pocketRocket.methods.spline3 import spline3_main

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("plotter.html")


@app.route('/proof')
def proof():
    return render_template("prueba.html")

@app.route('/grapher', methods=['GET', 'POST'])
def grapher():
    return render_template("plotter.html")


@app.route('/bisection', methods=['GET', 'POST'])
def bisection():
    form = rootAlgorithms()
    result = []
    message = []
    if request.method == 'POST':
        inter_a = form.inter_a.data
        inter_b = form.inter_b.data
        f_x = form.function.data
        n = form.n_max.data
        tol = form.tol.data
        x = symbols('x', real=True)
        parser = parse_expr(f_x, locals())
        data = biseccion(parser, inter_a, inter_b, n, tol)

        if len(data[1]):
            result = zip(*[i for i in data[1].values()])
        else:
            result = ""

        message = data[0]
        #form.result.data = result[1]

    return render_template("bisection.html", form=form, result=result, message=message)


@app.route('/incrementalSearch', methods=['GET', 'POST'])
def incremental_search():
    form = rootAlgorithms()
    result = []
    message = []
    if request.method == 'POST':
        f_x = form.function.data
        x_0 = form.x_0.data
        h = form.inter_h.data
        n = form.n_max.data
        tol = form.tol.data
        x = symbols('x', real=True)
        parser = parse_expr(f_x, locals())
        data = busqueda_incremental(parser, x_0, h, n, tol)
        result = zip(*[i for i in data[1].values()])
        message = data[0]
        #form.result.data = result

    return render_template("incremental_search.html", form=form, result=result, message=message)


@app.route('/falsePosition', methods=['GET', 'POST'])
def false_position():
    form = rootAlgorithms()
    result = []
    message = []
    if request.method == 'POST':
        f_x = form.function.data
        x_0 = form.x_0.data
        x_1 = form.x_1.data
        n = form.n_max.data
        tol = form.tol.data
        x = symbols('x', real=True)
        parser = parse_expr(f_x, locals())
        data = regla_falsa(f_x, x_0, x_1, tol, n)
        result = zip(*[i for i in data[1].values()])
        message = data[0]
        print (message)

    return render_template("false_position.html", form=form, result=result, message=message)


@app.route('/fixedPoint', methods=['GET', 'POST'])
def fixed_point():
    form = rootAlgorithms()
    result = []
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
        result = zip(*[i for i in result.values()])
        form.result.data = result

    return render_template("fixed_point.html", form=form, result=result)


@app.route('/secant', methods=['GET', 'POST'])
def secant():
    form = rootAlgorithms()
    result = []
    if request.method == 'POST':
        f_x = form.function.data
        x_0 = form.x_0.data
        x_1 = form.x_1.data
        tol = form.tol.data
        n = form.n_max.data
        x = symbols('x', real=True)
        parser = parse_expr(f_x, locals())
        result = secante_method(x_0, x_1, tol, n, parser)
        result = zip(*[i for i in result.values()])
        form.result.data = result

    return render_template("secant.html", form=form, result=result)


@app.route('/newton', methods=['GET', 'POST'])
def newton():
    form = rootAlgorithms()
    result = []
    if request.method == 'POST':
        f_x = form.function.data
        f_x_derivate = form.first_derivate.data
        x_n = form.x_0.data
        tol = form.tol.data
        n = form.n_max.data
        x = symbols('x', real=True)
        parser_f = parse_expr(f_x, locals())
        parser_f_derivate = parse_expr(f_x_derivate, locals())
        result = newton_method(x_n, tol, n, parser_f, parser_f_derivate)
        result = zip(*[i for i in result.values()])
        form.result.data = result

    return render_template("newton.html", form=form, result=result)


@app.route('/multipleRoots', methods=['GET', 'POST'])
def multiple_roots():
    form = rootAlgorithms()
    result = []
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
        result = multiple_roots_method(x_n, tol, parser_f, parser_f_derivate, parser_f_derivate_2)
        result = zip(*[i for i in result.values()])
        form.result.data = result

    return render_template("multiple_roots.html", form=form, result=result)


@app.route('/aitken', methods=['GET', 'POST'])
def aitken():
    pass
    return render_template("aitken.html")


@app.route('/muller', methods=['GET', 'POST'])
def muller():
    form = rootAlgorithms()
    result = []
    if request.method == 'POST':
        f_x = form.function.data
        x_0 = form.x_0.data
        x_1 = form.x_1.data
        x_2 = form.x_2.data
        x = symbols('x', real=True)
        parser = parse_expr(f_x, locals())
        result = muller_method(x_0, x_1, x_2, parser)
        form.result.data =  result

    return render_template("muller.html", form=form)


@app.route('/steffenson', methods=['GET', 'POST'])
def steffenson():
    form = rootAlgorithms()
    result = []
    if request.method == 'POST':
        f_x = form.function.data
        x_0 = form.x_0.data
        tol = form.tol.data
        n = form.n_max.data
        result = steff(f_x, x_0, tol, n)
        #form.result.data = result
        result = zip(*[i for i in result.values()])

    return render_template("steffenson.html", form=form, result=result)


@app.route('/gaussSimple', methods=['GET', 'POST'])
def gauss_simple():
    form = matrixAlgorithms()
    result=[]
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        b_solution = form.b_solution.data.split(" ")
        result = eliminacion(matrix_a, b_solution)
        form.result.data = result
        result = zip(*[i for i in result.values()])

    return render_template("gauss_simple.html", form=form, result=result)


@app.route('/gaussTotalPivot', methods=['GET', 'POST'])
def gauss_totalpivot():
    form = matrixAlgorithms()
    result=[]
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        instance = totalPivoting(matrix_a)
        result = instance.elimination()
        form.result.data = result
        result = zip(*[i for i in result.values()])

    return render_template("gauss_totalpivot.html", form=form, result=result)


@app.route('/gaussPartialPivot', methods=['GET', 'POST'])
def gauss_partialpivot():
    form = matrixAlgorithms()
    result=[]
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        b_solution = form.b_solution.data.split(" ")
        result = gaussPivPar(matrix_a, b_solution)
        form.result.data = result
        result = zip(*[i for i in result.values()])

    return render_template("gauss_partialpivot.html", form=form, result=result)


@app.route('/luSimpleGaussian', methods=['GET', 'POST'])
def lu_simple_gaussian():
    form = matrixAlgorithms()
    result=[]
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        n = form.n_max.data
        result = lu_simple_gauss(matrix_a, int(n))
        form.result.data = result
        result = zip(*[i for i in result.values()])

    return render_template("lu_simple_gaussian.html", form=form, result=result)


#Falta por implementar
@app.route('/luPivoting', methods=['GET', 'POST'])
def lu_pivoting():
    form = matrixAlgorithms()
    result=[]
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        result = lu_decomposition(matrix_a)
        form.result.data = result

    return render_template("lu_pivoting.html", form=form)


@app.route('/crout', methods=['GET', 'POST'])
def crout():
    form = matrixAlgorithms()
    result=[]
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        matrix_a = np.array(matrix_a)
        n = form.n_max.data
        result = crout_method(matrix_a, int(n))
        form.result.data = result
        result = zip(*[i for i in result.values()])

    return render_template("crout.html", form=form, result=result)


@app.route('/doolittle', methods=['GET', 'POST'])
def doolittle():
    form = matrixAlgorithms()
    result=[]
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        matrix_a = np.array(matrix_a)
        n = form.n_max.data
        result = doolittle_method(matrix_a, int(n))
        form.result.data = result
        result = zip(*[i for i in result.values()])

    return render_template("doolittle.html", form=form, result=result)


@app.route('/cholesky', methods=['GET', 'POST'])
def lucholeskypivoting():
    form = matrixAlgorithms()
    result=[]
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        matrix_a = np.array(matrix_a)
        n = form.n_max.data
        result = cholesky(matrix_a, int(n))
        form.result.data = result
        result = zip(*[i for i in result.values()])

    return render_template("cholesky.html", form=form, result=result)


@app.route('/jacobi', methods=['GET', 'POST'])
def jacobi():
    form = matrixAlgorithms()
    result=[]
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        x_0 = form.x_0.data.split(" ")
        n_max = form.n_max.data
        tol = form.tol.data
        instance = jacobiClass(n_max, tol, x_0, matrix_a)
        result = instance.jacobi_method()
        form.result.data = result
        result = zip(*[i for i in result.values()])
        print(result)

    return render_template("jacobi.html", form=form, result=result)


@app.route('/gaussSeidel', methods=['GET', 'POST'])
def gauss_seidel():
    form = matrixAlgorithms()
    result=[]
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        x_0 = form.x_0.data.split(" ")
        n_max = form.n_max.data
        tol = form.tol.data
        instance = seidelClass(n_max, tol, x_0, matrix_a)
        result = instance.gaussSeidel()
        form.result.data = result
        result = zip(*[i for i in result.values()])

    return render_template("gauss_seidel.html", form=form, result=result)


@app.route('/sor', methods=['GET', 'POST'])
def sor():
    form = matrixAlgorithms()
    result=[]
    if request.method == 'POST':
        matrix_a = np.matrix(form.matrix_a.data)
        matrix_a = np.array(matrix_a)
        b_solution = form.b_solution.data.split(" ")
        b_solution = [int(x) for x in b_solution]
        tol = form.tol.data
        w_sor = form.w_sor.data
        result = sor_method(matrix_a, b_solution, tol, w_sor)
        form.result.data = result
        result = zip(*[i for i in result.values()])

    return render_template("sor.html", form=form, result=result)


@app.route('/lagrange', methods=['GET', 'POST'])
def lagrange():
    form = interpolationAlgorithms()
    result=[]
    if request.method == 'POST':
        value = form.value.data
        x_points = form.x_points.data.split(" ")
        y_points = form.y_points.data.split(" ")
        result = lagrange_method(value, x_points, y_points)
        form.result.data = result

    return render_template("lagrange.html", form=form)


@app.route('/newtonPoly', methods=['GET', 'POST'])
def newton_interpolation():
    form = interpolationAlgorithms()
    result=[]
    if request.method == 'POST':
        n_max = form.n_max.data
        x_points = form.x_points.data.split(" ")
        y_points = form.y_points.data.split(" ")
        result = newton_inter(n_max, x_points, y_points)
        form.result.data = result

    return render_template("newton_interpolation.html", form=form)


@app.route('/vandermorde', methods=['GET', 'POST'])
def vandermorde():
    form = interpolationAlgorithms()
    result=[]
    if request.method == 'POST':
        x_points = form.x_points.data.split(" ")
        y_points = form.y_points.data.split(" ")
        result = vandermorde_method(x_points, y_points)
        form.result.data = result

    return render_template("vandermorde.html", form=form)


@app.route('/splines', methods=['GET','POST'])
def splines():
    form = interpolationAlgorithms()
    if request.method == 'POST':
        x_points = form.x_points.data.split(" ")
        y_points = form.y_points.data.split(" ")
        spline = int(form.spline.data)

        if spline == 1:
            result =  spline1_main(x_points, y_points)
            form.result.data = result
            result = zip(*[i for i in result.values()])
        
        elif spline == 2:
            pass
            #instance = splineQ(x_points, y_points)
            #instance.quadratic()

        else:
            result = spline3_main(x_points, y_points)
            form.result.data = result
            result = zip(*[i for i in result.values()])

    return render_template("splines.html", form=form)
