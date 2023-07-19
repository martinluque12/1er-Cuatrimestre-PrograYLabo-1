'''
1G MARTIN LUQUE

Ejercicio 08

Pedir al usuario que ingrese 5 números (verificar que sea un número, comprendido entre -1000 y 1000).
Mostrar:
1. Todos los números ingresados.
2. Suma de los positivos.
3. Producto de los negativos.
4. Promedio de todos los números.
'''
separator = '\n*-------------------------------------------------------------------*'

numbers = []

sum_positive_numbers = 0
product_negative_numbers = 1
sum_numbers = 0

for i in range(5):
    while True:
        try:
            entered_number = int(input('\n\nIngrese un numero entre -1000 y 1000 > ').strip())
            while entered_number < -1000 or entered_number > 1000:
                entered_number = int(input('\n¡Error! Debe ingresar un numero entre -1000 y 1000 > ').strip())
            break
        except ValueError:
            print('\n¡Error! Debe ingresar un dato numérico.')

    numbers.append(entered_number)

print(separator)

for number in numbers:
    print(f'\nSe ingresaron los siguientes números: {number}')

    if number > 0:
        sum_positive_numbers += number
    else:
        product_negative_numbers *= number

    sum_numbers += number

average_numbers = sum_numbers / len(numbers)

print(separator)

if sum_positive_numbers > 0:
    print(f'\nLa suma de los números positivos ingresados es {sum_positive_numbers}.')
else:
    print('\nNo se ingresaron números positivos.')

print(separator)

if product_negative_numbers != 1:
    print(f'\nEl producto de los números negativos ingresados es {product_negative_numbers}')
else:
    print('\nNo se ingresaron números negativos.')

print(separator)

print(f'\nEl promedio de todos los números ingresados es {average_numbers:.2f}')

print(separator)