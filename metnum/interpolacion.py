from . utils import debug_print, cstyle_for

def newton(x, y, punto_a_interpolar):
    if(len(x) != len(y)):
        raise Exception("Longitudes diferentes para vectores x,y")
    
    n = len(x)
    sumatoria = 0.0
    
    for j in cstyle_for(0, lambda j : j<n-1, lambda j : j+1):
        for i in cstyle_for(n-1, lambda i : i>j, lambda i : i-1):
            y[i] = (y[i] - y[i-1]) / (x[i] - x[i-j-1])
    
    for i in cstyle_for(n-1, lambda i : i>=0, lambda i : i-1):
        mult = 1.0
        for j in cstyle_for(0, lambda j : j<i, lambda j : j+1):
            mult *= (punto_a_interpolar - x[j])
        
        mult *= y[j]
        sumatoria += mult
    
    return sumatoria

def lagrange(x, y, punto_a_interpolar):
    if(len(x) != len(y)):
        raise Exception("Longitudes diferentes para vectores x,y")
    
    n = len(x)
    sumatoria = 0.0
    
    for i in cstyle_for(0, lambda i: i<=n-1, lambda i : i+1):
        mult = 1.0
        for j in cstyle_for(0, lambda j : j<=n-1, lambda j : j+1):
            if i!=j:
                mult *= (punto_a_interpolar - x[j]) / (x[i] - x[j])
        sumatoria += mult * y[i]
    
    return sumatoria
    
