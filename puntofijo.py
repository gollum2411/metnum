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

intro = """
      Metodos Numericos : Iteso 2013
Programa para calcular raices de una ecuacion
utilizando el metodo de punto fijo.

Para modificar la funcion a evaluar, abrir el
archivo y modificar la funcion func().
"""

#Funcion a trabajar
def func(punto):
    return -1 * math.pow(math.e, punto)


if __name__ == '__main__':
    print intro
    try:
        aprox = float(raw_input("Aproximacion: "))
        iteraciones = int(raw_input("Numero de iteraciones: "))
    except ValueError:
        sys.stderr.write("Entrada debe ser numerica")
        sys.exit(-1)
        
    x0 = aprox
    for i in range(iteraciones):
        temp = func(aprox)
        print "Iteracion = %d \t x0 = %.5f" % (i+1, temp)
        aprox = temp