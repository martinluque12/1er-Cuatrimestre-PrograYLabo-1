'''
1G MARTIN LUQUE

Ejercicio 13 Listas

Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario quiera 
(se limita a 1 perrito por ingreso), se les pide:
* Nombre 
* Precio de la consulta (validar entre 500$ y 2500$)
* Raza: (validar entre caniche, ovejero o Pitbull),
* Edad (validar 1 a 15)
* Peso (entre 25 y 40 kilos) 

Determinar:
1. Generar un listado con todos los datos de los pacientes ordenados por edad.
2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por nombre.
3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de impuesto por ingresos brutos e informarlo.
4. Informar el nombre y el peso del perro con más peso.
'''
separator = '\n=================================================================================='

patient_data = []
patient_over_30kg = []

gross_price = 0
weight_dog_over_30kg = None
flag_dog_over_30kg = True

while True:

    dog_name = input('\n\nIngrese el nombre del paciente > ').strip().capitalize()
    while not dog_name or not dog_name.isalpha():
        dog_name = input('\n¡Error! Este campo es obligatorio y/o solo acepta caracteres alfabéticos > ').strip().capitalize()

    dog_breed = input('\n\nIngrese la raza del paciente:\n\nCaniche\n\nOvejero\n\nPitbull\n\n> ').strip().lower()
    while dog_breed != "ovejero" and dog_breed != "caniche" and dog_breed != "pitbull":
        dog_breed = input('\n¡Error! Raza no valida, vuelva a intentarlo\n\nCaniche\n\nOvejero\n\nPitbull\n\n> ').strip().lower()

    while True:
        try:
            dog_age = int(input('\n\nIngrese la edad del paciente (Entre 1 y 15 años) > ').strip())
            while dog_age < 1 or dog_age > 15:
                dog_age = int(input('\n¡Error! Edad no valida vuelva a intentarlo > ').strip())
            break
        except ValueError:
            print('\n¡Error! Solo ingrese caracteres numéricos.')

    while True:
        try:
            dog_weight = int(input('\n\nIngrese el peso del paciente (Entre 25 y 40 kg) > ').strip())
            while dog_weight < 25 or dog_weight > 40:
                dog_weight = int(input('\n¡Error! Peso no valido vuelva a intentarlo > ').strip())
            break
        except ValueError:
            print('\n¡Error! Solo ingrese caracteres numéricos.')
    
    while True:
        try:
            consultation_price = int(input('\n\nIngrese el precio de la consulta (Entre $500 y $2500) > ').strip())
            while consultation_price < 500 or consultation_price > 2500:
                consultation_price = int(input('\n¡Error! Precio no valido, vuelva a intentarlo > ').strip())
            break
        except ValueError:
            print('\n¡Error! Solo ingrese caracteres numéricos.')

    patient_data.append([dog_name, dog_breed, dog_age, dog_weight, consultation_price])

    if dog_weight > 30:
        patient_over_30kg.append([dog_name, dog_breed, dog_age, dog_weight, consultation_price])
    
    gross_price += consultation_price
    
    answer = input('\n\n¿Quiere seguir ingresando pacientes? Responda con si o con no > ').strip().lower()
    while answer != "si" and answer != "no":
        answer = input('\n¡Error! Respuesta invalida. Responda con si o con no > ').strip().lower()
    if answer == "si":
        continue
    else:
        break

for i in range(len(patient_data)):
    min_index = i
    for j in range(i + 1, len(patient_data)):
        if patient_data[j][2] < patient_data[min_index][2]:
            min_index = j
    patient_data[i], patient_data[min_index] = patient_data[min_index], patient_data[i]

print(separator)

print('\nLista de pacientes ordenada por edad (de menor a mayor).')

for patient in patient_data:
    print(separator)
    print('\nNombre: {0}\nRaza: {1}\nEdad: {2} años\nPeso: {3}kg\nValor de la consulta: ${4}'.format(patient[0],
                                                                                                     patient[1].capitalize(),
                                                                                                     patient[2],
                                                                                                     patient[3],
                                                                                                     patient[4]))

print(separator)

for i in range(len(patient_over_30kg)):
    min_index = i
    for j in range(i + 1, len(patient_over_30kg)):
        if patient_over_30kg[j][0] < patient_over_30kg[min_index][0]:
            min_index = j
    patient_over_30kg[i], patient_over_30kg[min_index] = patient_over_30kg[min_index], patient_over_30kg[i]

print('\nLista de pacientes de mas de 30kg ordenada por nombre alfabéticamente.')

for patient in patient_over_30kg:
    weight = patient[3]
    print(separator)
    print('\nNombre: {0}\nRaza: {1}\nEdad: {2} años\nPeso: {3}kg\nValor de la consulta: ${4}'.format(patient[0],
                                                                                                     patient[1].capitalize(),
                                                                                                     patient[2],
                                                                                                     patient[3],
                                                                                                     patient[4]))
    if flag_dog_over_30kg or weight > weight_dog_over_30kg:
        weight_dog_over_30kg = patient[3]
        name_dog_over_30kg = patient[0]
        flag_dog_over_30kg = False

print(separator)

if gross_price > 5000:
    price_taxes = gross_price + (gross_price + 21) / 100
    print('\n\nPor haber superado los $5000 se debe agregar 21% de impuestos por ingresos brutos.')
    print(f'\nEl total es ${price_taxes:.2f}')
else:
    print(f'\n\nEl precio total de la consulta es ${gross_price:.2f}')

print(separator)

print(f'\n\nEl paciente con mayor peso es {name_dog_over_30kg} y su peso es {weight_dog_over_30kg}kg.')

print(separator)