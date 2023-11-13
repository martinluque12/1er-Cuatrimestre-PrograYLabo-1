'''
Coincidencias Basicas
.       - Cualquier Caracter, excepto nueva linea
\d      - Cualquier Digito (0-9)
\D      - No es un Digito (0-9)
\w      - Caracter de Palabra (a-z, A-Z, 0-9, _)
\W      - No es un Caracter de Palabra.
\s      - Espacios de cualquier tipo. (espacio, tab, nueva linea)
\S      - No es un Espacio, Tab o nueva linea.

Limites
\b      - Limite de Palabra
\B      - No es un Limite de Palabra
^       - Inicio de una cadena de texto
$       - Final de una cadena de texto

Cuantificadores:
*       - 0 o Más
+       - 1 o Más
?       - 0 o Uno
{3}     - Numero Exacto
{3,4}   - Rango de Numeros (Minimo, Maximo)

Conjuntos de Caracteres
[]      - Caracteres dentro de los brackets
[^ ]    - Caracteres que NO ESTAN dentro de los brackets

Grupos
( )     - Grupo
|       - Uno u otro

'''
import re

texto = "Esto es una frase para usar de modelo en la explicación de expresiones regulares"
texto1 = """
esto es una frase
esto es otra frase
direccion ip 192:23:076
finaliza con palabra
"""
# devuelve la primera ocurrencia, span=(donde empieza incluido y donde termina excluido)
# patron_encontrado = re.search("o",texto)

# print(patron_encontrado.start())#donde empieza
# print(patron_encontrado.end())# doonde termina
# print(patron_encontrado.group())#la primer ocurrencia
# print(patron_encontrado.span())#donde empieza donde termina

# devuelve una lista de las ocurrencias              tercer parametro opcional
# patron_encontrado = re.findall("MODELO", texto, re.IGNORECASE)
# print(patron_encontrado)

# {} en las llaves se ponen cuantas ocurrencias quiero buscar
# patron_encontrado = re.findall("i{2}", texto1, re.IGNORECASE)
# print(patron_encontrado)

# entre 1 y 4 ocurrencias
# patron_encontrado = re.findall("i{1,4}", texto1, re.IGNORECASE)
# print(patron_encontrado)

# nada o todas las "i"
# patron_encontrado = re.findall("i*", texto1, re.IGNORECASE)
# print(patron_encontrado)

# una frase que comience con...                   lee multilineas
# patron_encontrado = re.findall("^esto", texto1, re.MULTILINE)
# print(patron_encontrado)

#una frase que termina con                         lee multilineas
# patron_encontrado = re.findall("frase$", texto1, re.MULTILINE)
# print(patron_encontrado)

# busca un rango de la a la z minuscula 
# patron_encontrado = re.findall("[a-z]", texto1, re.MULTILINE)
# print(patron_encontrado)

# busca todas las e y todas las g
# patron_encontrado = re.findall("[eg]", texto1, re.MULTILINE)
# print(patron_encontrado)

#todos los caracteres alfanumericos y si es w mayuscula todo lo que no sea alfanumerico
#\s todo lo que es un espacio y S mayuscula todo lo que no sea un espacio
#\d todo los numeros D mayuscula todo lo que no es un numero
# patron_encontrado = re.findall("\d{2}", texto1, re.MULTILINE)
# print(patron_encontrado)

#todos los caracteres | si se pone por ejemplo "."+"rase" devuelve todo lo que contenga esas palabras juntas
# patron_encontrado = re.findall(".", texto1, re.MULTILINE)
# print(patron_encontrado)

email = "juanperez@hotmail.com "
#el @ y todo lo que viene atras
patron_encontrado = re.findall("@.+", email)
print(patron_encontrado)

#todo lo que viene despues del @ sin el @
# patron_encontrado = re.findall("@(.+)", email)
# print(patron_encontrado)

#que arranque con @ y todo lo que sigue menos el espacio
# patron_encontrado = re.findall("@[^ ]*", email)
# print(patron_encontrado)

#divide por el patron que se le pase y los agrega a una lista
# patron_encontrado = re.split("@", email)
# print(patron_encontrado)

#lo que quiero remplazar, por lo que voy a remplazar, la cadena, y a cuantos le quiero remplazar
# patron_encontrado = re.sub("@", "q", email, 1)
# print(patron_encontrado)
