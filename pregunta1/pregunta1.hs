--Nombre: Nestor Herrera
--Carnet: 18-10796


--Ejercicio b de la parte i de la pregunta 1--

-- definimos primero una recursion de cola que realizara el calculo requerido cuando m=0
conteoCola :: Integer -> Integer -> Integer
conteoCola m 1 = m
conteoCola m n = case mod n 2 of -- La funcion seq evalua el primer argumento, y devuelve el segundo. Esto fuerza a que m+1 se evalue lo antes posible
                        0 -> seq (m+1) $ conteoCola (m+1) (div n 2)
                        1 -> seq (m+1) $ conteoCola (m+1) (3*n + 1)

-- 
conteo :: Integer -> Integer
conteo = conteoCola 0

-- Ejercicio ii de la pregunta 1: mergesort

-- Primero definimos la funcion merge, que toma dos listas ordenadas y las une manteniendo el orden
-- La defino como recursion de cola porque soy fan d optimizar la pila (?)
-- Obtenemos el merge al tomar [] como primer argumento
-- Podria limitarme a enteros, pero realmente basta que sea un tipo que se pueda ordenar.
mergeCola :: Ord a => [a] -> [a] -> [a] -> [a]
-- Como Haskell es declarativo, debemos implementarlo como una recursion.
-- Hacemos recursion de cola: Lo que hemos calculado de la lista se guarda en p.
-- Caso base:
mergeCola p a [] = p ++ a -- Como a y b estan ordenados, si alguno de ellos es vacio, entonces el resultado estara ordenado
mergeCola p [] b = p ++ b
-- Caso recursivo:  Hacemos la llamada dependiendo de los valores de los heads de las listas
mergeCola p (as:a) (bs:b) = if as <= bs then seq (p ++ [as]) $ mergeCola (p ++ [as]) a (bs:b)
                            else seq (p ++ [bs]) $ mergeCola (p ++ [bs]) (as:a) b
                    --Conservamos el head que sea menor, y seguimos la recursion con el resto

--mergeSort
mergeSort :: Ord a => [a] -> [a]
-- Casos base
mergeSort [] = []
mergeSort [x] = [x]

-- Caso recursivo
-- take: toma los primeros n elementos de una lista
-- drop: toma todos los elementos de una lista excepto los primeros n
-- Hacemos las llamadas recursivas a mergeSort para asegurarnos de que los pedazos queden ordenados
mergeSort a = mergeCola [] (mergeSort (take mitad a)) (mergeSort (drop mitad a))
    where mitad = div (length a) 2