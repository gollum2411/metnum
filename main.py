import math
from metnum import raices

def func_punto_fijo(punto):
    """Funcion ejemplo para probar el metodo
    de punto fijo: y = e^(-x)"""
    return math.pow(math.e, -1*punto)

def func_biseccion(punto):
    """Funcion ejemplo para probar el metodo
    de biseccion: x^3 - x - 2"""
    return math.pow(punto, 3) - punto - 2

if __name__ == '__main__':
    print "*\**** Probando funcion punto_fijo *****"
    print raices.punto_fijo(0, func_punto_fijo, 10, True)
    print "*\**** Probando funcion biseccion *****"
    print raices.biseccion(1, 2, func_biseccion, 10, True)
    print "*\**** Probando funcion taylorcos *****"
    print raices.taylorcos(0.2, 10, True)