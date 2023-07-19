'''
1G MARTIN LUQUE

Ejercicio 07

Tomando como base el ejercicio anterior:
1. Contar los pares.
2. Encontrar el mas grande de los impares.
'''
even_number = []

largest_odd_number = None
flag_largest_odd_number = True

separator = '\n*--------------------------------------------------*'

for i in range(5):
    while True:
        try:
            entered_number = int(input('\n\nIngrese un numero entero > ').strip())
            break
        except ValueError:
            print('\n¡Error! Debe ingresar un dato numérico.')
    
    if entered_number % 2 == 0:
        even_number.append(entered_number)
    else:
        if flag_largest_odd_number or entered_number > largest_odd_number:
            largest_odd_number = entered_number
            flag_largest_odd_number = False

print(separator)

if even_number:
    if len(even_number) == 1:
        print(f'\nSe ingreso {len(even_number)} número par.')
    else:
        print(f'\nSe ingresaron {len(even_number)} números pares.')
else:
    print('\nNo se ingresaron números pares.')

print(separator)

if largest_odd_number != None:
    print(f'\nEl numero impar mas grande que se ingreso es {largest_odd_number}.')
else:
    print('\nNo se ingresaron números impares.')

print(separator)

