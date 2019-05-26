from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class rootAlgorithms(FlaskForm):
    function = StringField('f(x)')
    x_0 = StringField('X0')
    inter_h = StringField('h')
    inter_a = StringField('a')
    inter_b = StringField('b')
    tol = StringField('tol')
    n_max = StringField('n')
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
    calculate = SubmitField('Calculate')


class interpolationeAlgorithms(FlaskForm):
    n_max = StringField('n')
    x_points = StringField('x_points')
    y_points = StringField('y_points')
    value = StringField('value')
    calculate = SubmitField('Calculate')    