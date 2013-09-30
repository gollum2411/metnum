class _BisecEntry(object):
    def __init__(self, punto_a, punto_b, func, num_decs=5):
        #Funcion para calcular punto medio
        self._punto_medio = lambda a, b: (a+b) / float(2)
        #funcion a evaluar
        self.func = func
        self.a = punto_a
        self.b = punto_b
        self.f_a = func(punto_a)
        self.f_b = func(punto_b)
        self.c = self._punto_medio(punto_a, punto_b)
        self.f_c = func(self.c)
        self.faxfb = self.f_a * self.f_b
    
    def biseccionar(self):
        """Devolver tupla de nuevos puntos A y B para encontrar
        nuevo intervalo."""
        temp = self.f_a * self.f_c
        
        if temp < 0:
            return self.a, self.c
        else:
            return self.c, self.b
