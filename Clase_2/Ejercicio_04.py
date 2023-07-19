'''
1G MARTIN LUQUE

Ejercicio 04

La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para
la cocina de Industrias Wayne. Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras de ingredientes.
Se registra por cada compra:

1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).

Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de descuento sobre el precio bruto,
o si compro más de 300 kilos en total, tengo un 25% de descuento sobre el precio bruto.
Se desea saber:

A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.
'''
separator = '\n*----------------------------------------------------------------------------------------------*'

gross_price = 0
total_kg = 0

discount_one = 15
discount_two = 25

price_most_expensive_food = None
flag_most_expensive_food = True

for i in range(5):

    product_type = input('\n\nIngrese el tipo del alimento: "Animal", "Vegetal" o "Mezcla" > ').strip().lower()
    while product_type != "animal" and product_type != "vegetal" and product_type != "mezcla":
        product_type= input('\n¡Error! Ingrese un tipo de alimento valido > ').strip().lower()

    while True:
        try:
            weight_kg = int(input('\n\nIngrese el peso en Kilogramos (Mínimo 10kg, máximo 100kg) > ').strip())
            while weight_kg < 10 and weight_kg > 100:
                weight_kg = int(input('\n¡Error! Peso no valido, vuelva a ingresarlo (Mínimo 10kg, máximo 100kg) > ').strip())
            break
        except ValueError:
            print('\n¡Error! Debe ingresar un valor numérico.')

    while True:
        try:
            price_kg = int(input('\n\nIngrese el precio por kg > ').lower())
            while price_kg < 0:
                price_kg = int(input('\n¡Error! El precio no puede ser negativo. Vuelva a ingresar el precio por kg > ').strip())
            break
        except ValueError:
            print('\n¡Error! Debe ingresar un valor numérico.')

    purchase_price = price_kg * weight_kg
    
    gross_price += purchase_price

    total_kg += weight_kg

    if flag_most_expensive_food or price_kg > price_most_expensive_food:
        price_most_expensive_food = price_kg
        most_expensive_food = product_type
        flag_most_expensive_food = False


print(separator)

print(f'\nPrecio bruto sin descuento: ${gross_price}')

print(separator)


if total_kg > 100 and total_kg < 300:
    discount_price = gross_price - (gross_price * discount_one) / 100
    print(f'\nPor haber comprado mas de 100kg tiene un descuento del 15% el importe total es ${discount_price:.2f}')
    print(separator)

elif total_kg > 300:
    discount_price = gross_price - (gross_price * discount_two) / 100
    print(f'\nPor haber comprado mas de 300kg tiene un descuento del 25% el importe total es ${discount_price:.2f}')
    print(separator)

print(f'\nEl tipo de alimento mas caro es {most_expensive_food.capitalize()}')

print(separator)

average_price_kg = gross_price / total_kg

print(f'\nPromedio de precio por kilogramo: ${average_price_kg:.2f}')

print(separator)
    