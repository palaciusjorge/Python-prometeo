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
#print(contador_letras('Hola Mundo')) Ejemplo de uso
'''
Dada una lista de números, obtén una nueva lista con el doble de cada valor. 
Usa la función map().'''
def multiplicador(lista_enteros):
    multiplied_list = list(map( lambda x: x*2, lista_enteros))
    return multiplied_list
#print(multiplicador([1, 2, 3])) Ejemplo de uso

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
#print(palabra_en_palabra(['manzana', 'banana', 'pera', 'manzanilla'], 'manza')) Ejemplo de uso
'''
Genera una función que calcule la diferencia entre los valores de dos listas.
Usa la función map().
'''
def diferencia_listas(lista_enteros1, lista_enteros2):
    resultado = list(map(lambda x, y: x - y, lista_enteros1, lista_enteros2))
    return resultado
#print(diferencia_listas([10, 8, 6], [1, 2, 3])) Ejemplo de uso
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
#print(calculadora_media([6, 7, 5])) Ejemplo de uso
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
#print(factorial(5)) Ejemplo de uso
'''
Genera una función que convierta una lista de tuplas a una lista de strings. 
Usa la función map().
'''
def tupla_to_string(lista_tuplas):
    lista_string = (list(map(lambda tupla: f"({', '.join(map(str, tupla))})", lista_tuplas)))
    return lista_string
#print(tupla_to_string([(1,2), (3,4)])) Ejemplo de uso
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
#print(division_excepciones()) Ejemplo de uso (requiere input)
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
#print(filtrar_nombres(['Perro', 'Mapache', 'Gato'])) Ejemplo de uso
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
#print(promedio_lista()) Ejemplo de uso (requiere input)
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
#print(introducir_edad()) Ejemplo de uso (requiere input)
'''
Genera una función que, al recibir una frase, 
devuelva una lista con la longitud de cada palabra. 
Usa la función map().
'''
def longitud_palabras(frase):
    lista_palabras = frase.split()
    lista_longitudes = list(map(lambda palabra: len(palabra), lista_palabras))
    return lista_longitudes
#print(longitud_palabras('Esto es una prueba')) Ejemplo de uso
'''
Genera una función que, para un conjunto de caracteres, 
devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
Las letras no pueden estar repetidas. Usa la función map().
'''
def tuplas_mayus_minus(cadena):
    lista_tuplas = list(set(map(lambda c: (c.lower(), c.upper()), cadena)))
    return lista_tuplas
#print(tuplas_mayus_minus('AbA')) Ejemplo de uso
'''
Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. 
Usa la función filter().
'''
def filtrar_palabras_por_letra(lista_palabras, letra):
    lista_filtrada = list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))
    return lista_filtrada
#print(filtrar_palabras_por_letra(['ana','antonio','pepe'], 'a')) Ejemplo de uso
'''
Crea una función lambda que sume 3 a cada número de una lista dada.
'''
def sumar_tres_lista(lista_numeros):
    lista_resultado = list(map(lambda x: x + 3, lista_numeros ))
    return lista_resultado
#print(sumar_tres_lista([1,2,3])) Ejemplo de uso
'''
Escribe una función que tome una cadena de texto y un número entero n como parámetros 
y devuelva una lista de todas las palabras que sean más largas que n. 
Usa la función filter().
'''
def filtrar_palabras_longitud(cadena_texto, n):
    lista_palabras = cadena_texto.split()
    lista_filtrada = list(filter(lambda palabra: len(palabra) >= n), lista_palabras)
    return lista_filtrada
#print(filtrar_palabras_longitud('uno dos tres cuatro', 4)) Ejemplo de uso
'''
Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
'''
from functools import reduce
def concatenar_numeros(lista_numeros):
    numero_concatenado = reduce(lambda x, y: str(x) + str(y), lista_numeros)
    return int(numero_concatenado)
#print(concatenar_numeros([5,7,2])) Ejemplo de uso
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
#print(listado_estudiantes()) Ejemplo de uso
def filtrar_diccionarios(lista_diccionarios_estudiantes):
    lista_filtrada = list(filter(lambda diccionario: diccionario.get("calificacion") >= 90, lista_diccionarios_estudiantes))
    return lista_filtrada
#print(filtrar_diccionarios(listado_estudiantes())) Ejemplo de uso
'''
Crea una función lambda que filtre los números impares de una lista dada.
'''
def filtrar_numeros_impares(lista_numeros):
    lista_impares = list(filter(lambda x: x%2 != 0, lista_numeros))
    return lista_impares
#print(filtrar_numeros_impares([1,2,3,4,5])) Ejemplo de uso
'''
Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. 
Usa la función filter().
'''
def filtrar_enteros(lista_mixta):
    lista_enteros = list(filter(lambda x: isinstance(x, int), lista_mixta))
    return lista_enteros
#print(filtrar_enteros([1,'a',2,'3'])) Ejemplo de uso
'''
Crea una función que calcule el cubo de un número dado mediante una función lambda.
'''
def cubo_lambda(numero):
    cubo = lambda x: x**3
    return cubo(numero)
#print(cubo_lambda(3)) Ejemplo de uso
'''
Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
'''
def producto_lista(lista_numeros):
    producto_total = reduce(lambda x,y: x*y, lista_numeros)
    return producto_total
#print(producto_lista([2,3,4])) Ejemplo de uso
'''
Concatena una lista de palabras. Usa la función reduce().
'''
def concatenar_palabras(lista_palabras):
    frase_concatenada = reduce(lambda x, y: x + " " + y, lista_palabras)
    return frase_concatenada
#print(concatenar_palabras(['Hola','mundo'])) Ejemplo de uso
'''
Calcula la diferencia total en los valores de una lista. Usa la función reduce().
'''
def diferencia_total(lista_numeros):
    diferencia = reduce(lambda x,y: x-y, lista_numeros)
    return diferencia
#print(diferencia_total([100, 20, 10, 5])) Ejemplo de uso
'''
Crea una función que cuente el número de caracteres en una cadena de texto dada.
'''
def contar_caracteres(cadena_texto):
    return len(cadena_texto)
#print(contar_caracteres('ejemplo')) Ejemplo de uso
'''
Crea una función lambda que calcule el resto de la división entre dos números dados.
'''
def resto_division(num1, num2):
    resto = lambda x, y: x%y
    return resto(num1, num2)
#print(resto_division(10,3)) Ejemplo de uso
'''
Crea una función que calcule el promedio de una lista de números.
'''
def promedio_numeros(lista_numeros):
    promedio = sum(lista_numeros)/len(lista_numeros)
    return promedio
#print(promedio_numeros([4,6,8])) Ejemplo de uso
'''
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada. 
'''
def buscar_duplicado(lista_elementos):
    elementos_vistos = set()
    for elemento in lista_elementos:
        if elemento in elementos_vistos:
            return elemento
        elementos_vistos.add(elemento)
    return None
#print(buscar_duplicado([1,2,3,2,4])) Ejemplo de uso
'''
Crea una función que convierta una variable en una cadena de texto y 
enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
'''
def enmascarar_cadena(variable):
    cadena = str(variable)
    if len(cadena) <= 4:
        return cadena
    else:
        enmascarada = '#' * (len(cadena) - 4) + cadena[-4:]
        return enmascarada
#print(enmascarar_cadena(1234567890)) Ejemplo de uso
'''
Crea una función que determine si dos palabras son anagramas, es decir, 
si están formadas por las mismas letras pero en diferente orden.
'''
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
#print(son_anagramas("Roma", "Amor")) Ejemplo de uso
'''
Crea una función que solicite al usuario ingresar una lista de nombres 
y luego un nombre para buscar en esa lista. 
Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; 
de lo contrario, lanza una excepción.
'''
def buscar_nombre_en_lista():
    try:
        lista_nombres = input("Introduce una lista de nombres separados por comas: \n")
        lista_nombres = [nombre.strip().lower() for nombre in lista_nombres.split(",")]
        nombre_a_buscar = input("Introduce el nombre a buscar: \n").strip().lower()
        if nombre_a_buscar in lista_nombres:
            return f"El nombre {nombre_a_buscar.capitalize()} fue encontrado en la lista."
        else:
            raise ValueError(f"El nombre {nombre_a_buscar.capitalize()} no fue encontrado en la lista.")
    except ValueError as e:
        return str(e)
#print(buscar_nombre_en_lista()) Ejemplo de uso (requiere input)
'''
Crea una función que tome un nombre completo y una lista de empleados, 
busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; 
de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
'''
def buscar_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado.get("nombre_completo").lower() == nombre_completo.lower():
            return empleado.get("puesto")
    return "La persona no trabaja aquí."
#print(buscar_empleado("Juan Pérez", [{"nombre_completo": "Ana Gómez", "puesto": "Gerente"}, {"nombre_completo": "Juan Pérez", "puesto": "Desarrollador"}])) Ejemplo de uso
'''
Crea una función lambda que sume elementos correspondientes de dos listas dadas.
'''
def sumar_listas(lista1, lista2):
    lista_suma = list(map(lambda x, y: x + y, lista1, lista2))
    return lista_suma
#print(sumar_listas([1,2,3], [4,5,6])) Ejemplo de uso
'''
Crea la clase Arbol
Define un árbol genérico con un tronco y ramas como atributos.
Métodos disponibles: 
crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, 
info_arbol.
Código a seguir:
Inicializar un árbol con un tronco de longitud 1 
y una lista vacía de ramas.
Implementar el método crecer_tronco para aumentar 
la longitud del tronco en una unidad.
Implementar el método nueva_rama para agregar una 
nueva rama de longitud 1 a la lista de ramas.
Implementar el método crecer_ramas para aumentar en 
una unidad la longitud de todas las ramas existentes.
Implementar el método quitar_rama para eliminar una 
rama en una posición específica.
Implementar el método info_arbol para devolver 
información sobre la longitud del tronco, 
el número de ramas y sus longitudes.
Caso de uso:
        a. Crear un árbol.
        b. Hacer crecer el tronco una unidad.
        c. Añadir una nueva rama.
        d. Hacer crecer todas las ramas una unidad.
        e. Añadir dos nuevas ramas.
        f. Retirar la rama situada en la posición 2.
        g. Obtener información sobre el árbol.
'''
class Arbol:
    def __init__(self, tronco: int, ramas: list):
        self.tronco = tronco
        self.ramas = ramas

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
Arbol_ejemplo = Arbol(1, [])
Arbol_ejemplo.crecer_tronco()
Arbol_ejemplo.nueva_rama()
Arbol_ejemplo.crecer_ramas()
Arbol_ejemplo.nueva_rama()
Arbol_ejemplo.nueva_rama()
Arbol_ejemplo.quitar_rama(2)
info = Arbol_ejemplo.info_arbol()
'''
Doble print porque no había definido el tipo
de dato en el inicializador y no realizaba el print
'''
#print("info:", info) 
#print(type(info))
'''
Crea la clase UsuarioBanco
Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
Código a seguir:
Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
Implementar agregar_dinero para aumentar el saldo del usuario.
Caso de uso:
        a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
        b. Agregar 20 unidades al saldo de Bob.
        c. Transferir 80 unidades de Bob a Alicia.
        d. Retirar 50 unidades del saldo de Alicia.

'''
class UsuarioBanco:
    def __init__(self, nombre: str, saldo: float, cuenta_corriente: bool):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    def retirar_dinero(self, cantidad: float):
        if cantidad > self.saldo:
            raise ValueError("Fondos insuficientes para retirar")
        self.saldo -= cantidad
    def transferir_dinero(self, otro_usuario, cantidad: float):
        if cantidad > self.saldo:
            raise ValueError("Fondos insuficientes para transferir")
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad
    def agregar_dinero(self, cantidad: float):
        self.saldo += cantidad
    def info_usuario(self):
        return {
            "nombre": self.nombre,
            "saldo": self.saldo,
            "cuenta_corriente": self.cuenta_corriente
        }
#Usuario1 = UsuarioBanco("Alicia", 100, True)
#Usuario2 = UsuarioBanco("Bob", 50, True)
#Usuario2.agregar_dinero(20)
#try:
    #Usuario2.transferir_dinero(Usuario1, 80)
#except ValueError as e:
    #print(e)
#try:
    #Usuario1.retirar_dinero(50)
#except ValueError as e:
    #print(e)
#print(Usuario1.info_usuario())
'''
Crea una función llamada procesar_texto
Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
Código a seguir:
Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
Caso de uso:
Verificar el funcionamiento completo de procesar_texto.
'''
def contar_palabras(texto):
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)
def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra.lower() != palabra_a_eliminar.lower()]
    return ' '.join(palabras_filtradas)
def procesar_texto(texto, opcion, *args): #Con un option imprimiendolo por pantalla?
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se requieren dos argumentos: palabra_original y palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se requiere un argumento: palabra_a_eliminar")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")
# Ejemplo de uso:
texto_ejemplo = "Hola mundo hola"
info = procesar_texto(texto_ejemplo, "contar")
print(info)
'''
Genera un programa que nos indique si es de noche, 
de día o de tarde según la hora proporcionada por el usuario.
'''
def what_time_of_day():
    try:
        hora = int(input("Introduce la hora (0-23): \n"))
        if hora < 0 or hora > 23:
            return "La hora debe estar entre 0 y 23"
        elif 6 <= hora < 12: #Horario genérico; el horario en España sería de 8:00 a 14:00
            return "Es por el día"
        elif 12 <= hora < 20: #Horario genérico; el horario en España sería de 14:00 a 21:00
            return "Es por la tarde"
        else:
            return "Es de noche"
    except ValueError:
        return "Debes introducir un número entero entre 0 y 23"
'''
Se puede hacer importando datetime para obtener la hora actual
from datetime import datetime
current_hour = datetime.now().hour
'''
#print(what_time_of_day()) Ejemplo de uso (requiere input)
'''
Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
Reglas:
        0 - 69: insuficiente
        70 - 79: bien
        80 - 89: muy bien
        90 - 100: excelente
'''
def calificacion_texto():
    try:
        calificacion = float(input("Introduce la calificación numérica (0-100): \n"))
        if calificacion < 0 or calificacion > 100:
            return "La calificación debe estar entre 0 y 100"
        elif calificacion < 70:
            return "Insuficiente"
        elif calificacion < 80:
            return "Bien"
        elif calificacion < 90:
            return "Muy bien"
        else:
            return "Excelente"
    except ValueError:
        return "Debes introducir un número entre 0 y 100"
#print(calificacion_texto()) Ejemplo de uso (requiere input)
'''
Escribe una función que tome dos parámetros: figura (una cadena que puede ser 
"rectangulo", "circulo" o "triangulo") 
y datos (una tupla con los datos necesarios para calcular el área de la figura).
'''
import math
def calcular_area(figura, datos):
    if figura == "rectangulo":
        if len(datos) != 2:
            raise ValueError("Se requieren dos datos: base y altura")
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        if len(datos) != 1:
            raise ValueError("Se requiere un dato: radio")
        radio = datos[0]
        return math.pi * radio ** 2
    elif figura == "triangulo":
        if len(datos) != 2:
            raise ValueError("Se requieren dos datos: base y altura")
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Figura no válida. Usa 'rectangulo', 'circulo' o 'triangulo'.")
#print(calcular_area("rectangulo", (5, 10))) Ejemplo de uso
#print(calcular_area("circulo", (7,))) Ejemplo de uso
#print(calcular_area("triangulo", (4, 8))) Ejemplo de uso
'''
Escribe un programa en Python que utilice condicionales para determinar 
el monto final de una compra en una tienda en línea, después de aplicar un descuento. 
El programa debe:
    a. Solicitar al usuario el precio original de un artículo.
    b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    e. Mostrar el precio final de la compra, considerando o no el descuento.
    f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.
'''
def calcular_precio_final():
    try:
        precio_original = float(input("Introduce el precio original del artículo: \n"))
        tiene_cupon = input("¿Tienes un cupón de descuento? (si/no): \n").strip().lower()
        if tiene_cupon == "si":
            valor_cupon = float(input("Introduce el valor del cupón de descuento: \n"))
            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon
            else:
                return "El valor del cupón debe ser mayor a cero."
        elif tiene_cupon == "no":
            precio_final = precio_original
        else:
            return "Respuesta no válida. Debes responder 'si' o 'no'."
        return f"El precio final de la compra es: {precio_final:.2f}"
    except ValueError:
        return "Debes introducir valores numéricos válidos."
#print(calcular_precio_final()) Ejemplo de uso (requiere input)

