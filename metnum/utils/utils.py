import sys
import os
import math

def debug_print(msg, debug):
    if debug:
        sys.stdout.write(msg + "\n")

def calcular_error(nuevo, viejo):
    try:
        return math.fabs((nuevo - viejo)/nuevo)
    except ZeroDivisionError:
        return 0
