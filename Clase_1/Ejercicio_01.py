'''
1G MARTIN LUQUE

Ejercicio 01

La división de higiene está trabajando en un control de stock para productos sanitarios.
Debemos realizar la carga de una compra de productos de prevención de contagio, de cada una debe obtener
los siguientes datos:

· El tipo ("barbijo", "jabón" o "alcohol")
· El precio
· La cantidad de unidades
· La marca
· El fabricante

Se debe informar los datos de la compra procesados para poder iniciar el control de stock.
'''

products = []
total_price = 0

while True:

    product_type = input('\n\nIngrese el tipo de producto que desea cargar: (Alcohol, Barbijo o Jabón) > ').strip().lower()
    while product_type != "alcohol" and product_type != "barbijo" and product_type != "jabon":
        product_type = input('\n¡Producto no valido! Inténtelo nuevamente. > ').strip().lower()
    
    while True:
        try:
            producto_price = float(input('\n\nIngrese el precio del producto. > ').strip())
            while producto_price < 0:
                producto_price = float(input('\nEl precio ingresado no puede ser negativo, vuelva a ingresarlo. > ').strip())
            break
        except ValueError:
            print('\n¡Error! Debe ingresar un valor numérico.')

    while True:
        try:
            product_units = int(input('\n\nIngrese la cantidad del producto. > ').strip())
            while product_units < 0:
                product_units = int(input('\nLa cantidad ingresada no puede ser negativa, vuelva a ingresarla. > ').strip())
            break
        except ValueError:
            print('\n¡Error! Debe ingresar un valor numérico.')

    product_band = input('\n\nIngrese el nombre de la marca del producto. > ').strip()
    while not product_band:
        product_band = input('\n¡Error! El nombre de la marca del producto no puede estar vacía, vuelva a ingresarla. > ').strip()
        continue

    product_manufacturer = input('\n\nIngrese el nombre del fabricante del producto. > ').strip()
    while not product_manufacturer:
        product_manufacturer = input('¡Error! El nombre del fabricante no puede estar vacío, vuelva a intentarlo. > ').strip()

    product = {
        'product': product_type,
        'price': producto_price,
        'units': product_units,
        'band': product_band,
        'manufacturer': product_manufacturer
    }

    products.append(product)

    answer = input('\n\n¿Quiere seguir ingresando productos? Responda con "si" o "no". > ').strip()
    while not answer or answer != "si" and answer != "no":
        answer = input('\n¡Error! Debe responder con si o con no. Vuelva a intentarlo. > ').strip()
    if answer == "no":
        break
    else:
        continue


print('\n\n==========================================================================================')
print('\nProducto      |      Precio      |      Cantidad      |      Marca      |      Fabricante')

for product in products:
    total_price_product = product['price'] * product['units']
    total_price += total_price_product

    print('\n{0:<13} |      ${1:<10} |          {2:<9} |      {3:<10} |      {4}'.format(product['product'].capitalize(),
                                                                                         product['price'],
                                                                                         product['units'], 
                                                                                         product['band'].capitalize(), 
                                                                                         product['manufacturer'].capitalize()))

print('\n                                        Total: ${}'.format(total_price))

print('\n\n==========================================================================================')    