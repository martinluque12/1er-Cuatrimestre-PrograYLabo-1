#crear un string.
cadena_uno = "Hola, mundo!"
cadena_dos = "Chau mundo"

#longitud de la cadena.
longitud = len(cadena_uno)

#acceder a x carácter de la cadena.
primer_caracter = cadena_uno[0]

#obtiene una nueva cadena desde el segundo carácter hasta el cuarto. 
subcadena = cadena_uno[1:5]  

#concatenar cadenas.
cadena_concatenada = cadena_uno + cadena_dos

#repetir cadena
cadena_repetida = cadena_uno * 3

# Convertir a mayúsculas
mayusculas = cadena_uno.upper()

# Convertir a minúsculas
minusculas = cadena_uno.lower()

# Reemplazar texto
nueva_cadena = cadena_uno.replace("Hola", "Saludos")

# Encontrar la posición de una subcadena
posicion = cadena_uno.find("mundo")

#método format
nombre = "Juan"
edad = 25
mensaje = "Hola, me llamo {} y tengo {} años.".format(nombre, edad)

#f-string
mensaje_f = f"Hola, me llamo {nombre} y tengo {edad} años."

#comparación de cadenas.
resultado = cadena_uno == cadena_dos

#verificar si un string se encuentra en una cadena.
contiene_subcadena = "mundo" in cadena_uno

#Divide la cadena en una lista utilizando un carácter especifico como separador.
partes = cadena_uno.split(",")  

#elimina espacios en blanco delante y detrás de un string.
cadena_sin_espacios = "   Hola   ".strip()

#método join (une elementos de una lista en un string)
lista_palabras = ["Hola", "mundo"]
cadena_unida = " ".join(lista_palabras)

#verifica si los caracteres de una cadena son dígitos numéricos
es_numero = cadena_uno.isdigit()

#verifica si los caracteres de una cadena son letras.
es_letra = cadena_uno.isalpha()

#verifica si los caracteres de una cadena son alfanuméricos.
es_alfanumerico = cadena_uno.isalnum()

#devuelve la cantidad de ocurrencias de un caracteres especificado en una cadena.
cantidad_de_ocurrencias = cadena_uno.count("a")

#devuelve una cadena con la primer letra en mayúscula.
primera_mayuscula = cadena_uno.capitalize()

















