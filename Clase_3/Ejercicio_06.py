'''
1G MARTIN LUQUE

Ejercicio 06

Pedir al usuario que ingrese 5 números enteros, mostrar solo los pares.
'''
even_number = []

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

for number in even_number:
    print(separator)
    print(f'\nEstos son los números pares ingresados {number}.')

print(separator)

    
        