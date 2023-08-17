'''
1G MARTIN LUQUE

Ejercicio 17 Listas

Realizar un programa que pida una palabra al usuario y determine si la palabra ingresada es un palíndromo o no.
De serlo deberá imprimir la palabra por consola.
'''
separator = "\n**************************************************************************************"

list_entered_word = []

entered_word = input('\nIngrese una palabra para verificar si es un palíndromo o no > ').lower().strip()

list_entered_word.append(entered_word)

for word in list_entered_word:

    if entered_word == word[::-1]:
        print(separator)
        print(f'\nLa palabra {entered_word} es un palíndromo, si se lee de derecha a izquierda es {word[::-1]}.')
        print(separator)
    else:
        print(separator)
        print(f'\nLa palabra {entered_word}, no es un palíndromo, si se lee de derecha a izquierda es {word[::-1]}.')
        print(separator)

            


