from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

class rootAlgorithms(FlaskForm):
    function = StringField('f(x)')
    function_g = StringField('g(x)')
    first_derivate = StringField('f`(x)')
    second_derivate = StringField('f``(x)')
    g_function = StringField('g(x)')
    x_0 = StringField('X0')
    x_1 = StringField('X1')
    x_2 = StringField('X2')
    inter_h = StringField('h')
    inter_a = StringField('a')
    inter_b = StringField('b')
    tol = StringField('Tol')
    n_max = StringField('n')
    result = TextAreaField('Result')
    calculate = SubmitField('Calculate')


class matrixAlgorithms(FlaskForm):
    matrix_a = StringField('A')
    b_solution = StringField('b_sol')
    n_max = StringField('n')
    w_sor = StringField('w')
    tol = StringField('tol')
    x_0 =  StringField('x0')
    x_points = StringField('x_points')
    y_points = StringField('y_points')
    result = TextAreaField('Result')
    calculate = SubmitField('Calculate')


class interpolationAlgorithms(FlaskForm):
    n_max = StringField('n')
    x_points = StringField('x_points')
    y_points = StringField('y_points')
    spline = StringField('spline')
    value = StringField('Value')
    result = TextAreaField('Result')
    calculate = SubmitField('Calculate')    
