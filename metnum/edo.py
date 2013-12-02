from . utils import debug_print

import sys
import os
import math

def euler(func, x_a, x_b, y_a, num_steps, debug=False):
    """Aproxima la EDO, recibiendo los valores x_a y x_b (valores
    inicial y final de la variable independiente), y_a (valor inicial en variable
    dependiente) y el numero de incrementos num_steps."""
    altura = (x_b - x_a) / float(int(num_steps))
    x = x_a
    y = y_a
    for iteracion in xrange(num_steps):
        debug_print("Iteracion: %d" % (iteracion+1), debug)
        debug_print("\tx = %f" % x, debug)
        debug_print("\ty = %f" % y, debug)
        y += altura * func(x,y)
        x += altura
    return y

def heun(func, x_a, x_b, y_a, num_steps, debug=False):
    x = x_a
    y = y_a
    h = (x_b - x_a) / float(num_steps)
    h2 = h*0.5
    
    for iteracion in range(num_steps+1):
        debug_print("Iteracion: %d" % (iteracion+1), debug)
        eval_xy = func(x,y)
        nueva_y = eval_xy
        y_predictor = y + h * eval_xy
        y = y + h2 * (nueva_y + func(x+h, y_predictor))
        x = x + h
        debug_print("\tY predictor: %f" % y_predictor, debug)
        debug_print("\tY corrector: %f" % y, debug)
    
    return y
    
def ralston(func, x0, y0, h, num_steps, debug=False):
    h3 = float(2/3) * h
    h4 = h / float(4)
    
    for iteracion in range(num_steps):
        debug_print("Iteracion: %d" % (iteracion+1), debug)
        k1 = func(x0, y0)
        y0 += h4 * (k1+3.0 * func(x0+h3, y0 + h3 * k1))
        x0 += h
        debug_print("x = %.5f\ty = %.5f" % (x0, y0), debug)
    
    return y0
    
def runge_kutta(func, x0, y0, h, num_steps, debug=False):
    h2 = h / float(2)
    h6 = h / float(6)
    
    for iteracion in range(num_steps):
        debug_print("Iteracion: %d" % (iteracion+1), debug)
        k1 =  func(x0, y0)
        k2 = func(x0 + h2, y0 + h2*k1)
        k3 = func(x0 + h2, y0 + h2*k2)
        k4 = func(x0 + h, y0 + h*k3)
        y0 = y0 + h6 * (k1 + 2*k2 + 2*k3 + k4)
        x0 = x0 + h
        debug_print("x = %.5f\ty = %.5f" % (x0, y0), debug)
    
    return y0

def punto_medio(func, x0, y0, h, num_steps, debug=False):
    h2 = h/float(2)
    for iteracion in range(num_steps):
        debug_print("Iteracion: %d" % (iteracion+1), debug)
        mid_x = x0 + h2
        mid_y = y0 + h2 * func(x0, y0)
        y0 = y0 + h * func(mid_x, mid_y)
        x0 = x0 + h
        debug_print("x = %.5f\ty = %.5f" % (x0, y0), debug)
    
    return y0
    

    
