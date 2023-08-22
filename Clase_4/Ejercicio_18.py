'''
1G MARTIN LUQUE

Ejercicio 18 Listas

Se necesita un programa que solicite al usuario que ingrese una lista de números enteros de tamaño N.
El programa deberá remover el valor máximo y mínimo de la lista y luego calcular y mostrar el promedio
de los valores restantes y determinar si el promedio es mayor o menor que la diferencia entre el máximo y
el mínimo valor previamente removido.
'''
separator = 120 * '*'

list_numbers = []

flag_max_number = True
max_number = None
flag_min_number = True
min_number = None

sum_numbers = 0

while True:

    while True:
        try:
            entered_number = int(input('\nIngrese un numero > ').strip())
            break
        except ValueError:
            print('\nError, solo se permiten caracteres numéricos.')

    list_numbers.append(entered_number)

    answer = input('\n¿Quiere seguir ingresando números? Responda con si o con no > ').lower()
    while answer != "si" and answer != "no":
        answer = input('\n¡Error! Respuesta invalida. Responda con si o con no > ').strip().lower()
    if answer == "si":
        continue
    else:
        break

for number in list_numbers:
    if flag_max_number or number > max_number:
        max_number = number
        flag_max_number = False
    if flag_min_number or number < min_number:
        min_number = number
        flag_min_number = False

list_numbers.remove(min_number)
list_numbers.remove(max_number)

for number in list_numbers:
    sum_numbers += number
    average = sum_numbers / len(list_numbers)

difference = max_number - min_number

print('\n'+separator)
print('\nSe han eliminado el numero mas grande y mas chico ingresado.')
print('\n'+separator)
print('\nEl promedio de los números restantes es {0:.2f}'.format(average))
print('\n'+separator)

if average < difference:
    print('\nEl promedio es menor a a la diferencia entre el numero mas grande y mas chico ingresado.')
    print('\nLa diferencia es {0}'.format(difference))
else:
    print('\nEl promedio es mayor a a la diferencia entre el numero mas grande y mas chico ingresado.')
    print('\nLa diferencia es {0}'.format(difference))

print('\n'+separator)