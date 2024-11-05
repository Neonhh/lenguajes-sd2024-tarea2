def es_signo(elemento):
    return (elemento == "+" or elemento == "-" or elemento == "*" or elemento == "/")

#Dados dos operandos y el operador, verifica si hay que
#colocarle parentesis a la operacion respectiva.
def corregirPrecedencia(a,b, operador):

    # Si es necesario coloca los parentesis, ademas maneja un poco cosas de espaciado
    # En la impresion
    if ("+" in a or "-" in a):
        a = "(" + a + ") "
        b = " " + b
    if ("+" in b or "-" in b):
        b = " (" + b + ")"
        a = " " + a

    return a + operador + b

# Evalua la expresion dada utilizando preorder o postorder
def evaluar(order, expression):

    if order.upper() == "PRE":
        ## Para evaluar en preorder, primero se voltea el arreglo de la expresion
        expression = expression[::-1]
    elif order.upper() != "POST":
        print("Orden no reconocido. Opciones: PRE, POST")
        return

    
    # Se crea una pila vacia para guardar los operandos
    operandos = []

    # Se crea un diccionario para manejar las operaciones
    operaciones = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: b - a,
        "*": lambda a, b: a * b,
        "/": lambda a, b: b // a
    }

    for elemento in expression:
        # Para las operaciones, se guarda el resultado de operar los dos ultimos
        # numeros en la pila
        if es_signo(elemento):
            a = operandos.pop()
            b = operandos.pop()

            resultado = operaciones[elemento](a, b)
            operandos.append(int(resultado))
       
        else:
            try:
                operandos.append(int(elemento))
            except:
                print("La expresion tiene elementos no validos: " + elemento)
                return

    return operandos[0] #El resultado queda en la posicion 0 de la pila

#Dada una expresion en orden prefijo o postfijo, la muestra en orden infijo
def mostrar(order, expression):
    
    if order.upper() == "PRE":
        ## Para evaluar en preorder, primero se voltea el arreglo de la expresion
        expression = expression[::-1]
    elif order.upper() != "POST":
        print("Orden no reconocido. Opciones: PRE, POST")
        return
    
    #Se crea una pila para guardar los operandos
    operandos = []

    #Se crea un diccionario para manejar las operaciones
    operaciones = {
        "+": lambda a, b: a + " + " + b,
        "-": lambda a, b: b + " - " + a,
        "*": lambda a, b: corregirPrecedencia(a, b, "*"),
        "/": lambda a, b: corregirPrecedencia(b, a, "/")
    }

    for elemento in expression:
            
        if es_signo(elemento):
            #Guardaremos la operacion realizada en la pila
            a = operandos.pop()
            b = operandos.pop()

            operacion = operaciones[elemento](a, b)
            operandos.append(operacion)
            
        else:
            operandos.append(elemento)
    
    return operandos[0]