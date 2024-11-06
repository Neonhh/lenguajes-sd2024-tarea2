# Implementaciones de la pregunta 4
# Nombre: Nestor Herrera
# Carnet: 18-10796

# ((7 + 9) % 5) + 3 = 4
# ((9 + 6) % 5) + 3 = 3


# Implementacion recursiva
def fibRecursivo43(n):
    if n >= 0 and n < 12:
        return n
    else:
        return fibRecursivo43(n-3) + fibRecursivo43(n-2*3) + \
                fibRecursivo43(n-3*3) + fibRecursivo43(n-4*3)

# Implementacion recursiva de cola
# Esta es solo para el caso recursivo. a, b, c y d dependen de n
def fibCola43(n, a, b, c, d):
    if n >= 0 and n < 12:
        return d
    else:
        return fibCola43(n-3, b, c, d, a + b + c + d)

# Funcion auxiliar para la llamada recursiva de cola
# Calcula los valores que deben tener a, b, c y d para poder llegar
# a la posicion n
def fibCola43aux(n):
    if n >= 0 and n < 12: return n
    else: return fibCola43(n, n%3, n%3 + 3, n%3 + 6, n%3 + 9)

# Implementacion iterativa a partir de la implementacion recursiva de cola
def fibIter43(n):

    # Parentesis: aqui puedo corregir mas facilmente el tema
    # con el caso base por los multiples valores
    if n >= 0 and n < 12: return n
    
    # Los valores de a, b, c y d correspondientes a la llamada de la
    # funcion recursiva de cola
    a, b, c, d = n%3, n%3 + 3, n%3 + 6, n%3 + 9
    
    while (n >= 12):
        #Asignacion simultanea equivalente a llamar la funcion con nuevos argumentos
        n, a, b, c, d = n-3, b, c, d, a + b + c + d
    # Al llegar al caso base se devuelve d
    return d