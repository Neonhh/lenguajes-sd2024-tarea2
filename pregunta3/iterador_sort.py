lista = [1,3,3,2,1]

def partes(pivote, lista):
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return menores, iguales, mayores

def ordenar(lista):
    if not lista:
        return
    if len(lista) == 1:
        yield lista[0]
    else:
        pivote = lista[0]
        menores, iguales, mayores = partes(pivote, lista)
        for x in ordenar(menores):
            yield x
        for x in iguales:
            yield x
        for x in ordenar(mayores):
            yield x

for x in ordenar(lista):
    print(x, end = ' ')