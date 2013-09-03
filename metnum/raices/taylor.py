# Iteso 2013: Series de Taylor para la funcion coseno

import math
import sys

def elevar(_base, potencia):
    if potencia == 0: return 1
    ret_base = float(_base)
    for i in range(potencia-1):
        ret_base *= float(_base)
    
    return ret_base
    
def factorial(base):
    if base < 0:
        raise ValueError("No se permiten negativos")
    
    base = float(base)
    
    if base <= 1:
        return 1
    else:
        return base * float(factorial(base-1))

def taylorcos(x, iteraciones=30):
    acc = float(0)
    for i in range(iteraciones):
        acc += (elevar(-1, i) * elevar(x, 2*i)) / factorial(2*i)
    
    return acc

if __name__ == '__main__':
    p = raw_input("Punto a evaluar: ")
    try:
        p = float(p)
    except ValueError:
        sys.stderr.write("La entrada debe ser numerica\n")
        sys.exit(-1)
        
    print "taylorcos(%f) = %f" % (p, taylorcos(p))
    