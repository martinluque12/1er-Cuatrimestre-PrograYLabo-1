'''
1G MARTIN LUQUE 

Ejercicio 09 Sin usar listas

Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de autos que tienen disponible a la venta.
Para esto se necesita saber de cada auto: 

* la marca

* año del modelo

* el precio 

(validar los tipos de datos ingresados) y mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio
sin usar listas primero, y después usando listas y comparar la composición del código.
'''
separator = '\n*-----------------------------------------------------------------*'

current_year = 2023

while True:
    car_brand = input('\n\nIngrese la marca del auto > ').strip()
    while not car_brand:
        car_brand = input('\n¡Error! Este campo es obligatorio. Ingrese la marca del auto > ').strip()

    while True:
        try:
            car_year = int(input('\n\nIngrese el año del auto > ').strip())
            while car_year < 2000 or car_year > current_year:
                car_year = int(input('\n¡Error! Año invalido. Vuelva a intentarlo > ').strip())
            break
        except ValueError:
            print('\n¡Error! Debe ingresar un dato numérico.')

    while True:
        try:
            car_price = int(input('\n\nIngrese el precio del auto > ').strip())
            while car_price < 1000000:
                car_price = int(input('\n¡Error! Precio no valido, vuelva a intentarlo > ').strip())
            break
        except ValueError:
            print('\n¡Error! Debe ingresar un dato numérico.')

    print(separator)

    print('\nMarca del auto : {0}'.format(car_brand.capitalize()))

    print('\nAño del auto: {0}'.format(car_year))

    print('\nPrecio del auto: ${0}'.format(car_price))

    print(separator)

    answer = input('\n\n¿Quiere seguir ingresando autos? Responda con si o con no > ').strip().lower()
    if answer == "si":
        continue
    else:
        break
