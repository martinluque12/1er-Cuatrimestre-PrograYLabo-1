'''
1G MARTIN LUQUE

Ejercicio 08 Listas

Escribir un programa que le pida al usuario ingresar una lista de nombres de personas (previamente validada) y luego
le pidan 1 solo nombre en específico. Se debe buscar el nombre especifico en la lista de nombres y si esta presente
el programa deberá imprimir la posición del nombre en la lista, la posición de memoria donde se encuentra ese nombre
y la cantidad de caracteres que tiene el nombre, si no se encuentra, se deberá informar por pantalla.
'''
separator = 120 * '*'

flag_name = False

entered_name = input('\nIngrese nombres separados por un espacio cada uno (Mínimo 4) > ').lower().split()
while len(entered_name) < 4 or not all(char.isalpha() or char.isspace() for char in entered_name):
    print('\n¡Error! Mínimo debe ingresar 4 nombres y solo debe contener caracteres alfabéticos.')
    entered_name = input('\nReingrese los nombres > ').lower().split()

specific_name = input('\nIngrese un nombre para verificar si se encuentra en la lista > ').lower()

for name in entered_name:
    if name == specific_name:
        position = entered_name.index(specific_name)
        memory_position = id(name)
        nombre = name
        flag_name = True

print('\n'+separator)

if flag_name:
    message = f'\nEl nombre {specific_name.capitalize()} se encuentra en la posición {position+1}, '
    message += f'la posición en memoria es {memory_position} y tiene {len(specific_name)} caracteres.'
    print(message)
else:
    print(f'\nEl nombre {specific_name.capitalize()} no se encuentra en la lista.')

print('\n'+separator)
