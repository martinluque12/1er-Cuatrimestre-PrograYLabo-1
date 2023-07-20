'''
1G MARTIN LUQUE

Ejercicio 10 Listas

Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición de memoria es la que mas
ocurrencias tiene dentro de esa lista.
'''
separator = '\n********************************************************************************'

numbers = []

max_occurrences = None
flag_max_occurrences = True

while True:
    while True:
        try:
            entered_number = int(input('\n\nIngrese un numero > ').strip())
            while not entered_number:
                entered_number = int(input('\n¡Error! Este campo es obligatorio > ').strip())
            break
        except ValueError:
            print('\n¡Error! DEbe ingresar solo caracteres numéricos.')

    numbers.append(entered_number)

    answer = input('\n\n¿Quiere seguir ingresando números? Responda con si o con no > ').strip().lower()
    while answer != "si" and answer != "no":
        answer = input('\nRespuesta inválida, por favor responde con si o con no > ')
    if answer == "si":
        continue
    else:
        break
    
for number in numbers:
    occurrences = numbers.count(number)
    if flag_max_occurrences or occurrences > max_occurrences:
        max_occurrences = occurrences
        number_most_occurrences = number
        flag_max_occurrences = False

print(separator)

print('\nEl numero con mas ocurrencias es el {0}, tiene {1} ocurrencias y su dirección de memoria es {2}'.format(number_most_occurrences,
                                                                                                              max_occurrences,
                                                                                                              id(number_most_occurrences)))
print(separator)