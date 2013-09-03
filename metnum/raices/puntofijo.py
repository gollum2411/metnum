# Funcion a evaluar: e^x + x = 0
# Despejando : x = -e^x
# La funcion despejada es nuestra ecuacion de la forma
# x = g(x)
#
# El programa pedira una aproximacion de la raiz de la funcion.
# Ademas, se pedira el numero de iteraciones a correr.
#


import sys
import os
import math
from .. utils import debug_print

def punto_fijo(aproximacion, func, iteraciones=30, debug=False):
    """Aproximar la raiz de una funcion mediante el metodo
    de punto fijo.
    
    Esta funcion recibe el punto aproximacion a evaluar en
    func, iterando segun se especifique en iteraciones
    
    """
    debug_print("Inicia funcion punto_fijo", debug)
    aproximacion = round(float(aproximacion), 5)
    for i in range(iteraciones):
        temp = func(aproximacion)
        debug_print("Iteracion %d : x = %.5f" % (i+1, temp), debug)
        aproximacion = temp
    
    debug_print("Fin funcion punto_fijo", debug)
    return aproximacion
