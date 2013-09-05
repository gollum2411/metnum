from . utils import debug_print

import sys
import os
import math

from _metnumclasses import _BisecEntry

def taylorcos(x, iteraciones=30, debug=False):
    """Funcion para aproximar coseno utilizando
    series de Taylor"""
    acc = float(0)
    debug_print("Inicia funcion taylorcos", debug)
    for i in range(iteraciones):
        debug_print("Iteracion %d : %.5f" % (i+1, acc), debug)
        acc += (math.pow(-1, i) * math.pow(x, 2*i)) / math.factorial(2*i)
    
    debug_print("Fin funcion taylorcos", debug)
    return acc

def punto_fijo(aproximacion, func, iteraciones=30, debug=False):
    """Aproximar la raiz de una funcion mediante el metodo
    de punto fijo.
    
    Esta funcion recibe el punto aproximacion a evaluar en
    func, iterando segun se especifique en iteraciones.
    
    """
    debug_print("Inicia funcion punto_fijo", debug)
    aproximacion = round(float(aproximacion), 5)
    for i in range(iteraciones):
        temp = func(aproximacion)
        debug_print("Iteracion %d : x = %.5f" % (i+1, temp), debug)
        aproximacion = temp
    
    debug_print("Fin funcion punto_fijo", debug)
    return aproximacion

def biseccion(punto_a, punto_b, func, iteraciones=30, debug=False):
    """Aproximar la funcion func utilizando el metodo de biseccion,
    tomando el intervalo comprendido por los puntos punto_a y punto_b
    """
    to_print = \
"""\
A=%.5f\tB=%.5f\tf(A)=%.5f\tf(B)=%.5f\tC=%.5f\tf(C)=%.5f\
"""
    punto_a = float(punto_a)
    punto_b = float(punto_b)
    
    debug_print("Inicia funcion biseccion", debug)
    for iteracion in range(iteraciones):
        entrada = _BisecEntry(punto_a, punto_b, func)
        msg = to_print % (entrada.a, entrada.b,
                          entrada.f_a, entrada.f_b,
                          entrada.c, entrada.f_c)
        debug_print(msg, debug)
        punto_a, punto_b = entrada.biseccionar()
    debug_print("Fin funcion biseccion", debug)
    return entrada.c
