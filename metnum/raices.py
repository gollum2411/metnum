from . utils import debug_print, calcular_error

import sys
import os
import math

from _metnumclasses import _BisecEntry

NUM_MIN = sys.float_info[3]

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

def punto_fijo(aproximacion, func, iteraciones=30, debug=False, min_error=NUM_MIN):
    """Aproximar la raiz de una funcion mediante el metodo
    de punto fijo. Devuelve tupla (<aproximacion>, <error>)
    
    Esta funcion recibe el punto aproximacion a evaluar en
    func, iterando segun se especifique en iteraciones.
    
    """
    debug_print("Inicia funcion punto_fijo", debug)
    aproximacion = float(aproximacion)
    nuevo = 0
    viejo = 0
    error = 0
    for i in range(iteraciones):
        temp = nuevo = func(aproximacion)
        debug_print("Iteracion %d : x = %.5f" % (i+1, temp), debug)
        error = calcular_error(nuevo, viejo)
        viejo = nuevo
        aproximacion = temp
        if error <= min_error:
            debug_print("Fin funcion punto_fijo", debug)
            return aproximacion, error
    
    debug_print("Fin funcion punto_fijo", debug)
    return aproximacion, error

def biseccion(punto_a, punto_b, func, iteraciones=30, debug=False, min_error=NUM_MIN):
    """Aproximar la funcion func utilizando el metodo de biseccion,
    tomando el intervalo comprendido por los puntos punto_a y punto_b.
    Devuelve tupla (<aproximacion>, <error>)
    """
    to_print = \
"""\
A=%.5f\tB=%.5f\tf(A)=%.5f\tf(B)=%.5f\tC=%.5f\tf(C)=%.5f\terror=%.5f\
"""
    punto_a = float(punto_a)
    punto_b = float(punto_b)
    
    debug_print("Inicia funcion biseccion", debug)
    viejo = float(0)
    nuevo = float(0)
    error = float(0)
    for iteracion in range(iteraciones):
        entrada = _BisecEntry(punto_a, punto_b, func)
        nuevo = entrada.c
        error = calcular_error(nuevo, viejo)
        msg = to_print % (entrada.a, entrada.b,
                          entrada.f_a, entrada.f_b,
                          entrada.c, entrada.f_c, error)
        debug_print(msg, debug)
        punto_a, punto_b = entrada.biseccionar()
        viejo = nuevo
        
        if error <= min_error:
            debug_print("Fin funcion biseccion", debug)
            return entrada.c, error
        
    debug_print("Fin funcion biseccion", debug)
    return entrada.c, error
