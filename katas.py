#contador de letras 1
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
#Multiplicador elementos de lista de enteros con map 2
def multiplicador(lista_enteros):
    multiplied_list = list(map( lambda x: x*2, lista_enteros))
    return multiplied_list
#Comparativa lista de palabras y palabra objetivo 3
def palabra_en_palabra(lista_palabras, palabra_objetivo):
    lista_resultado = []
    for palabra in lista_palabras:
        if palabra_objetivo.lower() in palabra.lower():
            lista_resultado.append(palabra)
    return lista_resultado
#Diferencia entre listas usando map() 4
def diferencia_listas(lista_enteros1, lista_enteros2):
    resultado = list(map(lambda x, y: x - y, lista_enteros1, lista_enteros2))
    return resultado
#Calculadora media 5
def calculadora_media(lista_notas, nota_aprobado):
    nota_media = sum(lista_notas)/len(lista_notas)
    if nota_media >= nota_aprobado:
        return f"Estás aprobado! Tu nota media es: {nota_media}"
    else:
        return f"Has suspendido. Tu nota media es: {nota_media}"
#Recursiva factorial 6
def factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
        factorial(n)
    return resultado
#Lista de tuplas a string 7
def tupla_to_string(lista_tuplas):
    lista_string = (list(map(lambda tupla: f"({', '.join(map(str, tupla))})", lista_tuplas)))
    return lista_string
#Captura de excepciones 8
def division_excepciones():
    try:
        x = float(input("Introduce el dividendo: \n"))
        y = float(input("Introduce el divisor: \n"))
        return x/y
    except ArithmeticError:
        return "No se puede dividir por ceros"
    except ValueError:
        return "Debes introducir números"
#Uso de filter para quitar nombres de una lista 9
def filtrar_nombres(lista_nombres, lista_prohibidos):
    lista_filtrada = list(filter(lambda nombre: nombre not in lista_prohibidos, lista_nombres))
    return lista_filtrada
#Promedio lista con manejo de excepciones 10
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
    