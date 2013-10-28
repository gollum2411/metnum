from . utils import debug_print

def trapecios(funcion, punto_a, punto_b, num_trapecios=100000, debug=False):
    """Aproxima el area bajo la curva funcion desde punto_a hasta punto_b,
    iterando num_trapecios veces."""
    debug_print("Inicia funcion trapecios", debug)
    altura = (punto_b - punto_a) / num_trapecios
    s = funcion(punto_a) + funcion(punto_b)
    
    debug_print("s =", str(s))
    
    for iteracion in xrange(1, num_trapecios):
        s += 2 * funcion(punto_a + iteracion * altura)
        debug_print("s =", str(s))
    
    return s * altura/2

def simpson(funcion, punto_a, punto_b, puntos=100000, debug=False):
    """Aproxima el area bajo la curva funcion desde punto_a hasta punto_b
    utilizando el metodo de Simpson."""
    debug_print("Inicia funcion simpson", debug)
    altura = (punto_b - punto_a) / puntos
    s = funcion(punto_a) + funcion(punto_b)
    
    debug_print("s =", str(s))
 
    for iteracion in range(1, puntos, 2):
        s += 4 * funcion(punto_a + iteracion * altura)
        debug_print("s =", str(s))
        
    for iteracion in range(2, puntos-1, 2):
        s += 2 * funcion(punto_a + iteracion * altura)
        debug_print("s =", str(s))
 
    return s * altura / 3
