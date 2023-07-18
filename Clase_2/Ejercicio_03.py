"""
1G MARTIN LUQUE

Ejercicio 3

Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.

El televidente debe ingresar:

» Nombre del votante
» Edad del votante (debe ser mayor a 13)
» Género del votante (masculino, femenino, otro)
» El nombre del participante a quien le dará el voto positivo.

No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:

A. El promedio de edad de las votantes de género femenino

B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.

C. Nombre del votante más joven que votó a Nacho.

D. Nombre de cada participante y porcentaje de los votos qué recibió.

E. El nombre del participante que ganó el reality (El que tiene más votos)
"""
number_female_voters = 0
ages_female_voter = 0
number_male_voters = 0

youngest_voter = None
flag_youngest_voter = True

votes_nacho = 0
votes_julieta = 0
votes_marcos = 0

total_votes = 0

while True:
    voter_name = input("\n\nIngrese su nombre > ").strip().isalpha()
    while not voter_name:
        voter_name = (
            input(
                '\n¡Error! Este campo es obligatorio y solo deben ingresarse caracteres alfanuméricos. Ingrese su nombre > '
            ).strip().isalpha())

    while True:
        try:
            voter_age = int(input('\n\nIngrese su edad (Debe ser mayor de 13 años) > ').strip())
            while voter_age < 14:
                voter_age = int(input('\n¡Error! Debes ser mayor de 13 años, vuelva a ingresar su edad > ').strip())
            break
        except ValueError:
            print("\n¡Error! Debe ingresar un valor numérico.")

    voter_gender = input('\n\nIngrese su genero: "Masculino", "Femenino", "Otro" > ').lower().strip()
    while voter_gender != "masculino" and voter_gender != "femenino" and voter_gender != "otro":
        voter_gender = input('\n¡Error! Vuelva a intentarlo: "Masculino", "Femenino", "Otro" > ').lower().strip()

    voted_participant = input(
        '\n\nIngrese el nombre del participante al cual quiere darle un voto positivo: "Nacho", "Julieta" o "Marcos"  > '
    ).lower().strip()
    while voted_participant != "nacho" and voted_participant != "julieta" and voted_participant != "marcos":
        voted_participant = input('\n¡Error! Nombre no valido, vuelva a intentarlo > ').lower().strip()


    if voter_gender == "femenino":
        number_female_voters += 1
        ages_female_voter += voter_age
    elif voter_gender == "masculino":
        if voter_age >= 25 and voter_age <= 40 and voted_participant == "nacho" or voted_participant == "julieta":
            number_male_voters += 1

    if voted_participant == "nacho":
        votes_nacho += 1
        if votes_nacho > 0:
            if flag_youngest_voter or voter_age < youngest_voter:
                youngest_voter = voter_age
                flag_youngest_voter = False
            
    elif voted_participant == "julieta":
        votes_julieta += 1
    else:
        votes_marcos += 1


    answer = input('\n\n¿Quiere seguir votando? Responda con "si" o "no". > ').lower().strip()
    while not answer or answer != "si" and answer != "no":
        answer = input('\n¡Error! Debe responder con si o con no. Vuelva a intentarlo. > ').lower().strip()
    if answer == "no":
        break
    else:
        continue

total_votes = votes_nacho + votes_julieta + votes_marcos

print('\n\n*------------------------------------------------------------------------------------*')

if number_female_voters > 0:
    average_age_female_voters = ages_female_voter / number_female_voters
    print('\nPromedio de edades de las votantes de genero Femenino: {0}'.format(average_age_female_voters))
else:
    print('\nNo hubo votantes del genero Femenino.')

print('\n*------------------------------------------------------------------------------------*')

if number_male_voters > 0:
    if number_male_voters == 1:
        print('\nHubo {0} votante del genero masculino que voto a Nacho o a Julieta.'.format(number_male_voters))
    else:
        print('\nHubo {0} votantes del genero masculino que votaron a Nacho o a Julieta.'.format(number_male_voters))
else:
    print('\nNo hubo votantes del genero Masculino que hayan votado a Nacho o a Julieta.')

print('\n*------------------------------------------------------------------------------------*')

if votes_nacho > 0:
    percentage_votes_nacho = (votes_nacho / total_votes) * 100
    print('\nLa edad del votante mas joven que voto a Nacho es {0}'.format(youngest_voter))
else:
    percentage_votes_nacho = 0
    print('\nNacho no recibió votos.')

print('\n*------------------------------------------------------------------------------------*')

if votes_julieta > 0:
    percentage_votes_julieta = (votes_julieta / total_votes) * 100
else:
    percentage_votes_julieta = 0

if votes_marcos > 0:
    percentage_votes_marcos = (votes_marcos / total_votes) * 100
else:
    percentage_votes_marcos = 0

percentages = """
Porcentaje de votos recibidos para Nacho {0:.2f}%

Porcentaje de votos recibidos para Julieta {1:.2f}%

Porcentaje de votos recibidos para Marcos {2:.2f}%
"""
print(percentages.format(percentage_votes_nacho, percentage_votes_julieta, percentage_votes_marcos))

print('\n*------------------------------------------------------------------------------------*')

if votes_nacho > votes_julieta and votes_nacho > votes_marcos:
    winner = "Nacho"
elif votes_julieta > votes_marcos:
    winner = "Julieta"
else:
    winner = "Marcos"

print('\nEl ganador o ganadora de Gran Hermano 2023 es {0}'.format(winner))

print('\n*------------------------------------------------------------------------------------*')


