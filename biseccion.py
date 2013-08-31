import os
import sys
import math

#    FUNCION PARA TRABAJAR
def func(punto):
    # y = e^x + x
    return float(math.pow(math.e, punto) + punto)


class BisecEntry(object):
    def __init__(self, punto_a, punto_b, func, num_decs=5):
        #Funcion para calcular punto medio
        self._punto_medio = lambda a, b: (a+b) / float(2)
        #funcion a evaluar
        self.func = func
        self.a = punto_a
        self.b = punto_b
        self.f_a = round(func(punto_a), num_decs)
        self.f_b = round(func(punto_b), num_decs)
        self.c = self._punto_medio(punto_a, punto_b)
        self.f_c = round(func(self.c), num_decs)
        self.faxfb = self.f_a * self.f_b
    
    def biseccionar(self):
        """Devolver tupla de nuevos puntos A y B para encontrar
        nuevo intervalo."""
        if self.c < 0:
            return self.a, self.c
        elif self.c > 0:
            return self.c, self.b

class BisecTabla(object):
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
    
