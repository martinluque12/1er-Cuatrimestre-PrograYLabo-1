'''
1G MARTIN LUQUE

Ejercicio 11 Listas

La real academia española nos pide desarrollar un pequeño programa que contenga el diccionario de la lengua española
y su traducción al inglés. Para esto necesitamos un algoritmo que nos permita el ingreso de una palabra en español
y su traducción al ingles y guardarlo en una lista.
Si la palabra no existe, debemos agregarla, y si la palabra existe debemos informar que la palabra ya existe y
su índice dentro del listado, esta carga debe ser hasta que el usuario se canse de ingresar palabras.
Al finalizar se debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en inglés. 
Recordar validar los datos de forma correcta.
'''
separator = '\n*************************************************************'

dictionary = []

while True:

    word_spanish = input('\n\nIngrese una palabra en español > ').strip().capitalize()
    while not word_spanish and not word_spanish.isalpha:
        word_spanish = input('\n¡Error! Este campo es obligatorio y/o solo ingrese caracteres alfanuméricos > ').strip().capitalize()
    
    word_english = input('\n\nIngrese la traducción al ingles de la palabra en español que ingreso > ').strip().capitalize()
    while not word_english and not word_english.isalpha:
        word_english = input('\n¡Error! Este campo es obligatorio y/o solo ingrese caracteres alfanuméricos > ').strip().capitalize()

    if (word_spanish, word_english) in dictionary:
        print(f'\nLa palabra ya se encuentra cargada. Su indice es {dictionary.index((word_spanish, word_english)) + 1}')
    else:
        dictionary.append((word_spanish, word_english))
    
    answer = input('\n\n¿Quiere seguir ingresando palabras? Responda con si o con no > ').strip().lower()
    while answer != "si" and answer != "no":
        answer = input('\n¡Error! Respuesta invalida. Responda con si o con no > ').strip().lower()
    if answer == "si":
        continue
    else:
        break

print(separator)

print('\nPalabra en español    |    Traducción al Ingles')

for word in dictionary:
    print('\n     {0:<16} |         {1}'.format(word[0], word[1]))

print(separator)