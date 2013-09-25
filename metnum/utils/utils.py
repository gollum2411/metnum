import sys
import os
import math

def debug_print(msg, debug):
    if debug:
        sys.stdout.write(msg + "\n")

calcular_error = lambda nuevo, viejo : math.fabs((nuevo - viejo)/nuevo)
