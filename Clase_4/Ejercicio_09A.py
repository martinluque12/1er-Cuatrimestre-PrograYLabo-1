'''
1G MARTIN LUQUE 

Ejercicio 01 listas

Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de autos
que tienen disponible a la venta.
Para esto se necesita saber de cada auto: 

* la marca

* año del modelo

* el precio 

(validar los tipos de datos ingresados) y mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio
usando listas.
'''
separator = '\n*--------------------------------------------------*'

current_year = 2023
minimum_price = 1000000



while True:
    cars = []

    car_brand = input('\n\nIngrese la marca del auto > ').strip()
    while not car_brand:
        car_brand = input('\n¡Error! Este campo es obligatorio. Ingrese la marca del auto > ').strip()

    while True:
        try:
            car_year = int(input('\n\nIngrese el año del auto (Ejemplo 2010) > ').strip())
            while car_year < 2000 or car_year > current_year:
                car_year = int(input('\n¡Error! Ingrese un formato de año valido (Ejemplo 2010) > ').strip())
            break
        except ValueError:
            print('\n¡Error! Debe ingresar datos numéricos.')

    while True:
        try:
            car_price = int(input('\n\nIngrese el precio del auto > ').strip())
            while car_price < minimum_price:
                car_price = int(input('\n¡Error! Precio no valido, vuelva a intentarlo > ').strip())
            break
        except ValueError:
            print('\n¡Error! Debe ingresar datos numéricos.')

    cars.append([car_brand, car_year, car_price])

    for car in cars:
        print(separator)
        print('\nMarca: {0}\nModelo: {1}\nPrecio: ${2}'.format(car[0].capitalize(), car[1], car[2]))
        print(separator)


    answer = input('\n\n¿Quiere seguir ingresando autos? Responda con si o con no > ').strip().lower()
    if answer == "no":
        break
    else:
        continue




