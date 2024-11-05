# Pregunta 3
# Algoritmo para ordenar arreglo de enteros usando iteradores -inspirado en quicksort-
# Nombre: Nestor Herrera
# Carnet: 18-10796

# Separa la lista en los elementos menores, iguales y mayores al pivote
def partes(pivote, lista):
    menores = [x for x in lista if x < pivote]
    yield menores
    iguales = [x for x in lista if x == pivote]
    yield iguales
    mayores = [x for x in lista if x > pivote]
    yield mayores

# Iterador principal imprime los elementos de la lista dada en orden
def ordenar(lista):
    if not lista:
        return
    if len(lista) == 1:
        yield lista[0]
    else:
        pivote = lista[0]
        count = 0
        for sublista in partes(pivote, lista):
            count += 1
            if count == 2:  # son los elementos iguales, no es necesario ordenarlos (e intentarlo genera stack overflow ;))
                for x in sublista:
                    yield x
            else:
                for x in ordenar(sublista):
                    yield x

def main():
    # Leer input del usuario
    entrada = input("Introduce una lista de números separados por espacios: ")
    # Convertir la entrada en una lista de enteros
    lista = list(map(int, entrada.split()))
    # Ordenar la lista e imprimir los elementos en una sola línea
    for x in ordenar(lista):
        print(x, end=' ')
    print()  # Para agregar una nueva línea al final

if __name__ == "__main__":
    main()