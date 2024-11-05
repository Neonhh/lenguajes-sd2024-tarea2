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
merge :: [Integer] -> [Integer] -> [Integer]
-- Como Haskell es declarativo, debemos implementarlo como una recursion, Casos base:
merge a [] = a -- Como a y b estan ordenados, si alguno de ellos es vacio, entonces el resultado estara ordenado
merge [] b = b
-- Caso recursivo:  Hacemos la llamada dependiendo de los valores de los heads de las listas
merge (as:a) (bs:b) = case compare as bs of  --Conservamos el head que sea menor, y seguimos la recursion con el resto
                                LT -> as : merge a (bs:b)
                                GT -> bs : merge (as:a) b
                                EQ -> as : merge a b