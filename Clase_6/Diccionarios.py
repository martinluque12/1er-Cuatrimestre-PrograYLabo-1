# dict = {}

# dict["agregar_clave"] = "valor"

# #elimina clave valor
# del dict["clave"]

lista = []

for i in range(1):

    alumno = {}

    nombre = input("martin")

    alumno["nombre"] = nombre

    nota_uno = int(input("10"))

    alumno["nota_1"] = nota_uno

    nota_dos = int(input("8"))
    
    alumno["nota_2"] = nota_dos

    alumno["promedio"] = (alumno["nota_1"] + alumno["nota_2"]) / 2

    lista.append(alumno)


for alumno in lista:
    print("\nNombre: {0}".format(alumno["nombre"]))