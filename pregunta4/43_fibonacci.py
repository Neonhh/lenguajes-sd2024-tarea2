# Implementaciones de la pregunta 4
# Nombre: Nestor Herrera
# Carnet: 18-10796

# ((7 + 9) % 5) + 3 = 4
# ((9 + 6) % 5) + 3 = 3


# Implementacion recursiva
def fibRecursivo34(n):
    if n >= 0 and n < 12:
        return n
    else:
        return fibRecursivo34(n-3) + fibRecursivo34(n-2*3) + \
                fibRecursivo34(n-3*3) + fibRecursivo34(n-4*3)

# Implementacion recursiva de cola
# Esta da como resultado 9 si se llama con un caso base
def fibCola34(n, a=0, b=3, c=6, d=9):
    if n >= 0 and n < 12:
        return d
    else:
        return fibCola34(n-3, b, c, d, a + b + c + d)

# Esta es la implementacion para un caso mas general.
# Devuelve el resultado correcto aun en el caso base
def fibCola34aux(n):
    if n >= 0 and n < 12: return n
    else: return fibCola34(n, 0, 3, 6, 9)

# Implementacion iterativa a partir de la implementacion recursiva de cola
def fibIter34(n):

    # Parentesis: aqui puedo corregir mas facilmente el tema
    # con el caso base por los multiples valores
    if n >= 0 and n < 12: return n
    
    # Los valores de a, b, c y d correspondientes a la llamada de la
    # funcion recursiva de cola
    a, b, c, d = 0, 3, 6, 9
    
    while (n >= 12):
        #Asignacion simultanea equivalente a llamar la funcion con nuevos argumentos
        n, a, b, c, d = n-3, b, c, d, a + b + c + d
    # Al llegar al caso base se devuelve d
    return d
