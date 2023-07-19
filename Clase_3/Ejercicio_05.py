'''
1G MARTIN LUQUE

Ejercicio 05

Pedir al usuario que ingrese 5 números enteros, mostrar los valores ingresados y calcular la suma de los mismos.
'''
sum_numbers = 0

separator = '\n*--------------------------------------------*'

for i in range(5):
    while True:
        try:
            entered_number = int(input('\n\nIngrese un numero entero > ').strip())
            break
        except ValueError:
            print('\n¡Error! Debe ingresar números enteros.')
    
    sum_numbers += entered_number

print(separator)

print(f'\nLa suma de los números ingresados es {sum_numbers}')

print(separator)