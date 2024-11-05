# Pregunta 2
# Nombre: Nestor Herrera
# Carnet: 18-10796

#Importa las funciones del archivo funciones.py
from funciones import evaluar, mostrar

#Aqui decidimos que accion tomar dependiendo de los argumentos recibidos
def handle_action(arguments):
    
    order = arguments[1]
    expression = arguments[2:]
   
    if arguments[0] == "EVAL": print(evaluar(order, expression))
    elif arguments[0] == "MOSTRAR": print(mostrar(order, expression))
    else: print("Comando no reconocido. Opciones: EVAL, MOSTRAR, SALIR")
        

#En la funcion main, leemos el input del usuario y llamamos a la funcion handle_action
def main():
    print("Inicio del programa aritmethic_order. Opciones:\n"+
                        "EVAL <orden> <expr>\n"+
                        "MOSTRAR <orden> <expr>\n"+
                        "SALIR\n")
    while True:
        action = input("$> ")
        
        if action.upper() == "SALIR":
            break

        handle_action(action.split(" "))

if __name__ == "__main__":
    main()