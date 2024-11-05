# Respuesta 2 del examen 2

Nombre: Nestor Herrera
Carnet: 18-10796

En los 2 script de python que se encuentran en esta carpeta, se escribio el programa que dadas expresiones en orden pre-fijo o post-fijo, puede resolverlas, o escribirlas en orden in-fijo.

en `arithmethic_order.py` esta la logica para leer input del usuario y decidir que accion tomar. En `funciones.py` estan las implementaciones de la funcionalidad y otras funciones auxiliares.

Tambien esta la carpeta `tests`, donde se escribieron los tests y se coloco tambien el index.html con los resultados.

## Ejecucion del programa

En la consola, una vez en la carpeta donde se encuentran ambos scripts, usar el comando `python -u aritmethic_order.py`. Esto iniciara el programa y presentara las opciones seguidas del prompt. Para salir del programa, usar el comando `SALIR`

## Pruebas

Para las pruebas se utilizo pytest, y para evaluar la covertura se uso coverage. Los scripts usados para las pruebas se encuentran en la carpeta `tests`. Los tests reportan una cobertura del 92%, se pueden ver los resultados de coverage en `tests/index.html`.

Para ejecutarlos, en `pregunta2` se usa el comando `coverage run -m pytest tests`. Luego de esto, usar `coverage report` mostrara los resultados en consola, y usar `coverage html` generara una carpeta que contiene el archivo `index.html` donde se pueden ver los resultados.