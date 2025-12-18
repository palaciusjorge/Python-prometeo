# Python-prometeo
Repositorio para los ejercicios de Katas de Pyhton de Prometeo
Funcionamiento de las funciones:
contador_letras(texto)
1. Generamos un dicionario vacío
2. Recorremos nuestro texto caracter por caracter y entramos en un condicional:
2.1. Caracter " "(espacio) saltamos al siguiente
2.2. Caracter no existente en el diccionario aún: lo inicializamos con el contador a 1
2.3. Caracter existente en el diccionario: sumamos 1 al contador
3. Return del diccionario completo.