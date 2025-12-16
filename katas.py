'''
Escribe una función que reciba una cadena de texto como parámetro y devuelva 
un diccionario con las frecuencias de cada letra en la cadena. 
Los espacios no deben ser considerados.
'''
def contador_letras(texto):
    texto = texto.lower()
    contadores = {}
    for i in range(len(texto)):
        if texto[i] == " ":
            continue
        elif texto[i] in contadores:
            contadores[texto[i]] += 1
        else:
            contadores[texto[i]] = 1
    return contadores
'''
Dada una lista de números, obtén una nueva lista con el doble de cada valor. 
Usa la función map().'''
def multiplicador(lista_enteros):
    multiplied_list = list(map( lambda x: x*2, lista_enteros))
    return multiplied_list

'''
Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
La función debe devolver una lista con todas las palabras de la lista original 
que contengan la palabra objetivo.
'''
def palabra_en_palabra(lista_palabras, palabra_objetivo):
    lista_resultado = []
    for palabra in lista_palabras:
        if palabra_objetivo.lower() in palabra.lower():
            lista_resultado.append(palabra)
    return lista_resultado
'''
Genera una función que calcule la diferencia entre los valores de dos listas.
Usa la función map().
'''
def diferencia_listas(lista_enteros1, lista_enteros2):
    resultado = list(map(lambda x, y: x - y, lista_enteros1, lista_enteros2))
    return resultado
'''
Escribe una función que tome una lista de números como parámetro y un valor opcional 
nota_aprobado (por defecto 5). 
La función debe calcular la media de los números en la lista y determinar si la media 
es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; 
de lo contrario, "suspenso". 
La función debe devolver una tupla que contenga la media y el estado.
'''
def calculadora_media(lista_notas, nota_aprobado=5):
    nota_media = sum(lista_notas)/len(lista_notas)
    if nota_media >= nota_aprobado:
        return (nota_media, "Aprobado")
    else:
        return (nota_media, "Suspenso")
'''
Escribe una función que calcule el factorial de un número de manera recursiva.
'''
def factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
        factorial(n)
    return resultado
'''
Genera una función que convierta una lista de tuplas a una lista de strings. 
Usa la función map().
'''
def tupla_to_string(lista_tuplas):
    lista_string = (list(map(lambda tupla: f"({', '.join(map(str, tupla))})", lista_tuplas)))
    return lista_string
'''
Escribe un programa que pida al usuario dos números e intente dividirlos. 
Si el usuario ingresa un valor no numérico o intenta dividir por cero, 
maneja esas excepciones de manera adecuada y muestra un mensaje indicando si 
la división fue exitosa o no.
'''
def division_excepciones():
    try:
        x = float(input("Introduce el dividendo: \n"))
        y = float(input("Introduce el divisor: \n"))
        return x/y
    except ArithmeticError:
        return "No se puede dividir por ceros"
    except ValueError:
        return "Debes introducir números"
'''
Escribe una función que tome una lista de nombres de mascotas como parámetro y 
devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. 
Usa la función filter().
'''
def filtrar_nombres(lista_nombres):
    lista_prohibidos = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    lista_filtrada = list(filter(lambda nombre: nombre not in lista_prohibidos, lista_nombres))
    return lista_filtrada
'''
Escribe una función que reciba una lista de números y calcule su promedio. 
Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
'''
def promedio_lista():
    try:
        lista_numeros = input("Introduce una lista de números separados por comas: \n")
        lista_numeros = lista_numeros.split(",")
        lista_numeros = list(map(float, lista_numeros))
        promedio = sum(lista_numeros)/len(lista_numeros)
        return promedio
    except ValueError:
        return "Debes introducir solo números separados por comas"
    except ZeroDivisionError:
        return "La lista no puede estar vacía"
'''
Escribe un programa que pida al usuario que introduzca su edad. 
Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado 
(por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
'''
def introducir_edad():
    try:
        edad = int(input("Introduce tu edad: \n"))
        if edad < 0:
            return "La edad no puede ser negativa"
        elif edad > 120:
            return "La edad no puede ser mayor de 120 años"
        else:
            return f"Tienes {edad} años"
    except ValueError:
        return "Debes introducir un número entero"
'''
Genera una función que, al recibir una frase, 
devuelva una lista con la longitud de cada palabra. 
Usa la función map().
'''
def longitud_palabras(frase):
    lista_palabras = frase.split()
    lista_longitudes = list(map(lambda palabra: len(palabra), lista_palabras))
    return lista_longitudes
'''
Genera una función que, para un conjunto de caracteres, 
devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
Las letras no pueden estar repetidas. Usa la función map().
'''
def tuplas_mayus_minus(cadena):
    lista_tuplas = list(set(map(lambda c: (c.lower(), c.upper()), cadena)))
    return lista_tuplas
'''
Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. 
Usa la función filter().
'''
def filtrar_palabras_por_letra(lista_palabras, letra):
    lista_filtrada = list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))
    return lista_filtrada
'''
Crea una función lambda que sume 3 a cada número de una lista dada.
'''
def sumar_tres_lista(lista_numeros):
    lista_resultado = list(map(lambda x: x + 3, lista_numeros ))
    return lista_resultado
'''
Escribe una función que tome una cadena de texto y un número entero n como parámetros 
y devuelva una lista de todas las palabras que sean más largas que n. 
Usa la función filter().
'''
def filtrar_palabras_longitud(cadena_texto, n):
    lista_palabras = cadena_texto.split()
    lista_filtrada = list(filter(lambda palabra: len(palabra) >= n), lista_palabras)
    return lista_filtrada
'''
Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
'''
from functools import reduce
def concatenar_numeros(lista_numeros):
    numero_concatenado = reduce(lambda x, y: str(x) + str(y), lista_numeros)
    return int(numero_concatenado)
'''
Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes 
(nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación 
mayor o igual a 90.
'''
def listado_estudiantes():
    lista_estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 22, "calificacion": 85},
        {"nombre": "Marta", "edad": 19, "calificacion": 90},
        {"nombre": "Carlos", "edad": 21, "calificacion": 78},
    ]
    return lista_estudiantes
def filtrar_diccionarios(lista_diccionarios_estudiantes):
    lista_filtrada = list(filter(lambda diccionario: diccionario.get("calificacion") >= 90, lista_diccionarios_estudiantes))
    return lista_filtrada
'''
Crea una función lambda que filtre los números impares de una lista dada.
'''
def filtrar_numeros_impares(lista_numeros):
    lista_impares = list(filter(lambda x: x%2 != 0, lista_numeros))
    return lista_impares
'''
Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. 
Usa la función filter().
'''
def filtrar_enteros(lista_mixta):
    lista_enteros = list(filter(lambda x: isinstance(x, int), lista_mixta))
    return lista_enteros

