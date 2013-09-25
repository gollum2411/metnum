import math
from metnum import raices

def fuerza_por_unidad_area_bisec(punto):
    return (250 / (1+(0.4 / \
           (math.cos(0.5 * math.sqrt(punto * 1/10000000)))))) - punto

def fuerza_por_unidad_area_pf(punto):
    return (250 / (1+(0.4 / \
           (math.cos(0.5 * math.sqrt(punto * 1/10000000))))))


if __name__ == '__main__':
    print "Resolviendo ecuacion por biseccion..."
    aprox, error = raices.biseccion(170, 180, fuerza_por_unidad_area_bisec, debug=True, min_error=0.0001)
    
    print "Se encontro raiz %f con error %f" % (aprox, error)
    
    print "Resolviendo ecuacion por punto fijo..."
    aprox, error = raices.punto_fijo(170, fuerza_por_unidad_area_pf, debug=True, min_error=0.0001)
    
    print "Se encontro raiz %f con error %f" % (aprox, error)