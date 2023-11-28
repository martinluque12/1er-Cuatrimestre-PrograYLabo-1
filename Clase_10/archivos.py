# r = "lectura"
# w = "escritura"
# rb = "lectura binaria"
# wb = "escritura binaria"
# a = "escritura agregar contenido"
# open()abre el archivo
# close()cierra el archivo
# read()lee el archivo completo
# readline()lee la primer linea
# readlines()devuelve una lista de todo lo del archivo separado por cada salto de linea
# tell()#posicion
# seek()

# file = open("/home/martinluque/Escritorio/Programacion y Laboratorio 1/Clase 11/prueba.txt", "r")

# contenido = file.readline()#puedo poner el numero de caracteres que quiero que lea

# file.close()

# print(contenido)

with open ("Clase 11/prueba.txt", "r") as file:
    
    for linea in file:
        print(linea, end="")

