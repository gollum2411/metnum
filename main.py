import math
from metnum import raices

def func_punto_fijo(punto):
    return -1 * math.pow(math.e, punto)

def func_biseccion(punto):
    return math.pow(punto, 3) - punto - 2


if __name__ == '__main__':
    print raices.punto_fijo(-1, func_punto_fijo, 10, True)
    print raices.biseccion(1, 2, func_biseccion, 10, True)