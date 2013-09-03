import os
import sys
import math

from .. utils import debug_print

#    FUNCION PARA TRABAJAR
def func(punto):
    # y = e^x + x
    return float(math.pow(math.e, punto) + punto)


class _BisecEntry(object):
    def __init__(self, punto_a, punto_b, func):
        #Funcion para calcular punto medio
        self._punto_medio = lambda a, b: (a+b) / float(2)
        self._datos = dict()
        self._datos["A"] = round(float(punto_a), 5)
        self._datos["B"] = round(float(punto_b), 5)
        self._datos["f(A)"] = round(func(punto_a), 5)
        self._datos["f(B)"] = round(func(punto_b), 5)
        self._datos["C"] = round(self._punto_medio(punto_a, punto_b))
        self._datos["f(C)"] = round(func(self._datos["C"]), 5)
        self._datos["f(A)f(B)"] = self._datos["f(A)"] * self._datos["f(B)"]
    
    def biseccionar(self):
        """Devolver tupla de nuevos puntos A y B para encontrar
        nuevo intervalo."""
        if self._datos["C"] < 0:
            return self._datos["A"], self._datos["C"]
        elif self._datos["C"] > 0:
            return self._datos["C"], self._datos["B"]

class _BisecTabla(object):
    def __init__(self):
        self.rows = list()
    
    def nueva_entrada(self, entrada):
        self.rows.append(entrada)
    
    def imprimir(self, ):
        print "A\tB\tf(A)\tf(B)\tC\tf(C)\tf(A)*f(B)"
        for entry in self.rows:
            print "%.5f\t%.5f\t%.5f\t%.5f\t%.5f\t%.5f\t%s" % \
            (entry.a, entry.b, entry.f_a, entry.f_b, entry.c,
             entry.f_c, ("+" if entry.faxfb > 0 else "-"))

def biseccion(punto_a, punto_b, func, iteraciones=30, debug=False):
    punto_a = round(float(punto_a), 5)
    punto_b = round(float(punto_b), 5)
    
    debug_print("Inicia funcion biseccion", debug)
    for iteracion in range(iteraciones):
        entrada = _BisecEntry(punto_a, punto_b, func)
        debug_print(str(entrada._datos), debug)
        punto_a, punto_b = entrada.biseccionar()
    
    debug_print("Fin funcion biseccion", debug)
    return entrada._datos["C"]
    


if __name__ == '__main__':
    try:
        punto_a = float(raw_input("Punto A: "))
        punto_b = float(raw_input("Punto B: "))
    except ValueError:
        sys.stderr.out("La entrada debe ser numerica")
    
    tabla = BisecTabla()
    
    for iteracion in range(5):
        entrada = BisecEntry(punto_a, punto_b, func)
        tabla.nueva_entrada(entrada)
        punto_a, punto_b = entrada.biseccionar()
    
    tabla.imprimir()
    
