'''
1G MARTIN LUQUE 

Ejercicio 14 Listas 

Se nos pide realizar un programa que le pida al usuario el ingreso de números una N cantidad de veces y 
calcular la máxima diferencia en la secuencia de números ingresada.
'''
separator = '\n**********************************************************************'

numbers = []

flag_first_entry = True
min_entered_number = None
max_entered_number = None

while True:

    while True:
        try:
            entered_number = int(input('\n\nIngrese un numero > ').strip())
            break
        except ValueError:
            print('\n¡Error! Ingrese solo caracteres numéricos')
    
    numbers.append(entered_number)

    answer = input('\n\n¿Quiere seguir ingresando números? Responda con si o con no > ').strip().lower()
    while answer != "si" and answer != "no":
        answer = input('\n¡Error! Respuesta invalida. Responda con si o con no > ').strip().lower()
    if answer == "si":
        continue
    else:
        break

for number in numbers:
    if flag_first_entry or number > max_entered_number:
        max_entered_number = number
        flag_first_entry = False
    else:
        min_entered_number = number

difference = max_entered_number - min_entered_number
print(separator)

print('\n\nEl numero mas chico ingresado es {0} y el mas grande es {1}'.format(min_entered_number, max_entered_number))
print('\nY su diferencia es {0}'.format(difference))

print(separator)