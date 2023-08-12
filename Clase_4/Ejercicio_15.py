'''
1G MARTIN LUQUE

Ejercicio 15 Listas

Un grupo de cinco amigos se juntan para jugar una partida de CS:GO, deciden que van a jugar 10 partidas y necesitan realizar
datos estadísticos sobre las partidas jugadas. Para eso necesitan ingresar los siguientes datos en el siguiente orden
especifico:
nombre, edad, bajas confirmadas (el murió), muertes confirmadas (el mate a otro jugador).
Con esos datos se necesita saber:
• Nombre del jugador más joven.
• Jugador que más bajas tuvo.
• Jugador con menos muertes.
• El promedio de bajas del equipo.
• La cantidad de jugadores que tienen entre 20 y 30 años cuyas bajas están entre 10 y 20 
• El nombre y edad del jugador que más muertes tuvo (MVP)
Nota: los datos tienen que ingresar en 1 solo string separado por espacios, y ser almacenados en una lista, investigar que
función les permite lograrlo y como hacer una lista de listas.
'''
PLAYER = 5

separator = '\n**************************************************************************************************'

player_data = []

flag_first_entry = True

youngest_player = None
player_most_kills = None
player_fewest_deaths = None
player_most_deaths = None

total_deaths = 0

for p in range(PLAYER):
    print('\nDATOS DEL JUGADOR N°: ',p+1)
    print('\nIngrese los datos solicitados de una vez, separados por un espacio. Ej: "Martin 20 5 12".')

    data = input('\nIngrese: nombre, edad, bajas confirmadas y muertes confirmadas > ').split()
    while len(data) != 4:
        print('\n¡Error! Los datos solicitados son 4 ni mas ni menos.')
        data = input('\nReingrese: nombre, edad, bajas confirmadas y muertes confirmadas > ').split()
    
    while not all(char.isalpha() or char.isspace() for char in data[0]):
        print('\n¡Error! El nombre debe contener solo letras.')
        data[0] = input('\nReingrese el nombre > ')
    
    for i in range(1, 4):
        while not data[i].isdigit():
            print(f'\n¡Error! El valor de la posición {i + 1} debe ser un número.')
            data[i] = input(f'\nReingrese el valor de la posición {i + 1} > ')

    player_data.append(data)

players_in_range = []

for data in player_data:
    name = data[0]
    age = int(data[1])
    defeat = int(data[2])
    kills = int(data[3])

    if flag_first_entry or age < youngest_player:
        youngest_player = age
        name_youngest_player = name
    if flag_first_entry or defeat > player_most_kills:
        player_most_kills = defeat
        name_player_most_kills = name
    if flag_first_entry or kills < player_fewest_deaths:
        player_fewest_deaths = kills
        name_player_fewest_deaths = name
    if flag_first_entry or kills > player_most_deaths:
        player_most_deaths = kills
        name_player_most_deaths = name
        age_player_most_deaths = age
    
    flag_first_entry = False

    total_deaths += defeat

    if age > 19 and age < 31 and defeat > 9 and defeat < 21:
        players_in_range.append(name)

    average_defeats = total_deaths / PLAYER

print(separator)
print(f'\nEl jugador mas joven es: {name_youngest_player.capitalize()}.')
print(separator)
print(f'\nEl jugador con mas bajas fue: {name_player_most_kills.capitalize()}.')
print(separator)
print(f'\nEl jugador con menos muertes fue: {name_player_fewest_deaths.capitalize()}.')
print(separator)
print(f'\nPromedio de bajas del equipo: {average_defeats:.2f}')
print(separator)
print(f'\nLa cantidad de jugadores que tienen entre 20 y 30 años y cuyas bajas están entre 10 y 20 son {len(players_in_range)}')
print(separator)
print(f'\nEl jugador que tuvo mas muertes (El MVP) fue : {name_player_most_deaths.capitalize()} y su edad es: {age_player_most_deaths} años.')
print(separator)