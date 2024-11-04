--Ejercicio b de la parte ii de la pregunta ii
--Nombre: Nestor Herrera
--Carnet: 18-10796

-- definimos primero una recursion de cola que realizara el calculo requerido cuando m=0
conteoCola :: Integer -> Integer -> Integer
conteoCola m 1 = m
conteoCola m n = case mod n 2 of -- La funcion seq evalua el primer argumento, y devuelve el segundo. Esto fuerza a que m+1 se evalue lo antes posible
                        0 -> seq (m+1) $ conteoCola (m+1) (div n 2)
                        1 -> seq (m+1) $ conteoCola (m+1) (3*n + 1)

-- 
conteo :: Integer -> Integer
conteo = conteoCola 0