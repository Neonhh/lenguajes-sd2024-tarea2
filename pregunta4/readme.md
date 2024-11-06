# Respuesta 4 y pruebas
Nombre: Nestor Herrera
Carnet: 18-10796

En esta carpeta se encuentra el archivo `fibonacci43.py`, con las implementaciones respectivas de este primo de fibonacci en las 3 formas: Recursiva estandar, recursiva de cola e iterativa.

Tambien tenemos el archivo `comparaciones.py` (se logroooo), script donde se utilizan las librerias time y matplotlib de python para ver y graficar los tiempos que tarda cada implementacion en ejecutarse segun los valores de n. Se deja en esta carpeta tambien la imagen `comparaciones.png` donde se pueden observar los resultados de estas pruebas.

## Conclusiones

Al ejecutar el comando `python -u comparaciones.py` se nos muestra la grafica que podemos ver en `comparaciones.png`. Donde se puede observar a simple vista como aumenta la diferencia entre el tiempo de la forma recursiva estandar y las otras dos formas. Siendo estas ultimas al parecer identicas y de tiempo aproximadamente constante, mientras que el tiempo que tarda la forma estandar crece de forma exponencial y la diferencia empieza a crecer notablemente alrededor de n = 70.

Entonces, la diferencia no es mucha para valores relativamente pequenos de n, pero cuando empezamos ver valores que van a las decenas para n ya hay que empezar a planificar el uso de la iteracion o recursion de cola, que en realidad parecieran ser equivalentes en rendimiento.