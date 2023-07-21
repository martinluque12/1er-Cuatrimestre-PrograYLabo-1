'''
1G MARTIN LUQUE

Ejercicio 12

Debemos desarrollar un algoritmo que permita computar los votos del Senado de Berlin.
Se deberá ingresar el nombre de cada senador y si está Presente o no en la sesión.
Si el senador está presente, se deberá pedir el valor del voto.
El voto de los senadores berlineses puede ser Afirmativo, Negativo o Abstención (validar).
El valor por defecto para los senadores ausentes será Abstención. 
Se deberá Informar:

* Cantidad total de senadores.
* Cantidad de senadores presentes.
* Cantidad y porcentaje de votos afirmativos.
* Cantidad y porcentaje de votos negativos.
* Cantidad y porcentaje de abstenciones.
* Generar una lista de senadores por cada tipo de voto y mostrarlas por pantalla.
'''
separator = '\n========================================================================='
senators = 0
senators_present = 0

affirmative_votes = []
negative_votes = []
abstention_votes = []

while True:

    senator_name = input('\n\nIngrese el nombre del senador > ').strip().capitalize()
    while not senator_name or not senator_name.isalpha():
        senator_name = input('\n¡Error! Este campo es obligatorio y/o solo ingrese caracteres alfabéticos > ').strip().capitalize()

    is_present = input('\n\n¿Esta presente en la sesión? Responda con si o con no > ').strip().lower()
    while is_present != "si" and is_present != "no":
        is_present = input('\n¡Error! Solo responda con si o con no > ').strip().lower()
    
    if is_present == "si":
        senators_present += 1
        vote = input('\n\nValor del voto : "Afirmativo", "Negativo" o "Abstención" > ').strip().lower()
        while vote != "afirmativo" and vote != "negativo" and vote != "abstencion":
            vote = input('\n¡Error! Vuelva a intentarlo "Afirmativo", "Negativo" o "Abstención" > ').strip().lower()
    else:
        vote = "abstencion"
        

    if vote == "afirmativo":
        affirmative_votes.append(senator_name)
    elif vote == "negativo":
        negative_votes.append(senator_name)
    else:
        abstention_votes.append(senator_name)

    senators += 1

    answer = input('\n\n¿Quiere seguir ingresando Senadores? Responda con si o con no > ').strip().lower()
    while answer != "si" and answer != "no":
        answer = input('\n¡Error! Respuesta invalida. Responda con si o con no > ').strip().lower()
    if answer == "si":
        continue
    else:
        break

total_votes = len(affirmative_votes) + len(negative_votes) + len(abstention_votes)

print(separator)

print('\nEn total hay {0} senadores. \nSenadores presentes: {1} \nSenadores ausentes: {2}'.format(senators, 
                                                                                                  senators_present,
                                                                                                  (senators-senators_present)))

print(separator)

if not affirmative_votes:
    print('\nNo hubo votos afirmativos.')
    print('\nEl porcentaje de votos afirmativos es 0%')
else:
    percentage_votes_affirmative = (len(affirmative_votes) / total_votes) * 100
    print(f'\nHubo {len(affirmative_votes)} voto/s afirmativo/s.')
    print('\nEl porcentaje de votos afirmativos es {0:.2f}%'.format(percentage_votes_affirmative))
    print('\nSenadores que votaron afirmativamente:')
    for name in affirmative_votes:
        print(f'\n{name.capitalize()}')

print(separator)

if not negative_votes:
    print('\nNo hubo votos negativos.')
    print('\nEl porcentaje de votos negativos es 0%')
else:
    percentage_votes_negative = (len(negative_votes) / total_votes) * 100
    print(f'\nHubo {len(negative_votes)} voto/s negativo/s.')
    print('\nEl porcentaje de votos negativos es {0:.2f}%'.format(percentage_votes_negative))
    print('\nSenadores que votaron negativamente:')
    for name in negative_votes:
        print(f'\n{name.capitalize()}')

print(separator)

if not abstention_votes:
    print('\nNingún senador se abstuvo de votar.')
    print('\nEl porcentaje de abstención es 0%')
else:
    percentage_abstention = (len(abstention_votes) / total_votes) * 100
    print(f'\nHubo {len(abstention_votes)} senador/es que se abstuvo/abstuvieron de votar.')
    print('\nEl porcentaje de abstención es {0:.2f}%'.format(percentage_abstention))
    print('\nSenadores que se abstuvieron:')
    for name in abstention_votes:
        print(f'\n{name.capitalize()}')

print(separator)

