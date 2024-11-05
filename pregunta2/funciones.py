def es_signo(elemento):
    return (elemento == "+" or elemento == "-" or elemento == "*" or elemento == "/")

def evaluar(order, expression):

    if order.upper() == "PRE":
        ## Para evaluar en preorder, primero se voltea el arreglo de la expresion
        expression = expression[::-1]
    elif order.upper() != "POST":
        print("Orden no reconocido. Opciones: PRE, POST")
        return

    
    # Se crea una pila vacia para guardar los operandos
    operandos = []

    for elemento in expression:
        # Para las operaciones, se guarda el resultado de operar los dos ultimos
        # numeros en la pila
        if es_signo(elemento):
            a = operandos.pop()
            b = operandos.pop()

            if elemento == "+":
                operandos.append(a + b)
            elif elemento == "-":
                operandos.append(b - a)
            elif elemento == "*":
                operandos.append(a * b)
            elif elemento == "/":
                operandos.append(b // a)
        else:
            operandos.append(int(elemento))

    return operandos[0] #El resultado queda en la posicion 0 de la pila

def mostrar(order, expression):
    pass