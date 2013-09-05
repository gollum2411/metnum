class _BisecEntry(object):
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
        if self.f_c < 0 and self.f_a < 0:
            return self.c, self.b
        else:
            return self.a, self.c