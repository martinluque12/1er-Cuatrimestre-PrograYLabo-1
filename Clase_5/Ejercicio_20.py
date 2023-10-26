'''
1G MARTIN LUQUE 
Refactorizar con Match
1-Cargar lista 5 num
2-Mostrar el total de los números ingresados
3-Mayor
4-Menor
5-Pedir un num y decir si está en la lista
6-Pedir números e informar todos los indice dónde aparece
7-Vaciar lista
'''
import os

SEPARATOR = '*'

list_numbers = []

loaded_numbers = False

options_message = """
1 - Cargar numero. \n2 - Mostrar todos los números ingresados. \n3 - Mostrar el número mas grande ingresado.
4 - Mostrar el número mas chico ingresado. \n5 - Buscar número en la lista. \n6 - Ingresar número para buscar su indice.
7 - Vaciar lista. \n0 - Salir. \n\n> """

while True:
    os.system('cls')

    options = input(options_message)

    match (options):

        case "1":

            if not loaded_numbers:
                for i in range(5):
                    while True:
                        try:
                            print("\n" + SEPARATOR * 80)
                            entered_number = int(input("\nIngrese un numero entero > ").strip())
                            while not entered_number:
                                print("\n" + SEPARATOR * 80)
                                entered_number = int(input("\n¡Error! Debe ingresar caracteres numéricos"
                                                           "mayores a 0 > ").strip())
                            
                            list_numbers.append(entered_number)

                            break
                        except ValueError:
                            print("\n" + SEPARATOR * 80)
                            print("\n¡Error! Debe ingresar caracteres numéricos mayores a 0, vuelva a intentarlo.")
                            continue
                
                loaded_numbers = True

                print("\n" + SEPARATOR * 50)
                print("\nNúmeros cargados exitosamente.")
                print("\n" + SEPARATOR * 50)

            else:
                print("\n" + SEPARATOR * 50)
                print("\nYa se han cargado los números.")
                print("\n" + SEPARATOR * 50)

        case "2":
           
            if loaded_numbers:
                print("\nEstos son los números que se ingresaron: ")
                print("\n" + SEPARATOR * 20)
                for number in list_numbers:
                    print(number, end=' | ')
                print("\n" + SEPARATOR * 20)

            else:
                print("\n" + SEPARATOR * 50)
                print("\nPrimero debe ingresar los números.")
                print("\n" + SEPARATOR * 50)

        case "3":
            
            if loaded_numbers:
                max_number = list_numbers[0]
                for number in list_numbers:
                    if number > max_number:
                        max_number = number
                
                print("\n" + SEPARATOR * 50)
                print(f"\nEl numero mas grande ingresado es: {max_number}")
                print("\n" + SEPARATOR * 50)

            else:
                print("\n" + SEPARATOR * 50)
                print("\nPrimero debe ingresar los números.")
                print("\n" + SEPARATOR * 50)

        case "4":
            
            if loaded_numbers:
                min_number = list_numbers[0]
                for number in list_numbers:
                    if number < min_number:
                        min_number = number
                
                print("\n" + SEPARATOR * 50)
                print(f"\nEl numero mas chico ingresado es: {min_number}")
                print("\n" + SEPARATOR * 50)

            else:
                print("\n" + SEPARATOR * 50)
                print("\nPrimero debe ingresar los números.")
                print("\n" + SEPARATOR * 50)
            
        case "5":

            if loaded_numbers:
                while True:
                    try:
                        print("\n" + SEPARATOR * 70)
                        number_search = int(input("\nIngrese un numero para buscar si esta en la lista > ").strip())
                        while not number_search:
                            print("\n" + SEPARATOR * 70)
                            number_search = int(input("\n¡Error! Debe ingresar caracteres numéricos"
                                                        "mayores a 0 > ").strip())
                    
                        break
                    except ValueError:
                        print("\n" + SEPARATOR * 80)
                        print("\n¡Error! Debe ingresar caracteres numéricos mayores a 0, vuelva a intentarlo.")
                        continue
                
                number_found = False

                for number in list_numbers:
                    if number_search == number:
                        number_found = True

                print("\n" + SEPARATOR * 50)
                if (number_found):
                    print("\nEl numero ingresado se encuentra en la lista.")
                else:
                    print("\nEl numero ingresado no se encuentra en la lista.")
                print("\n" + SEPARATOR * 50)

            else:
                print("\n" + SEPARATOR * 50)
                print("\nPrimero debe ingresar los números.")
                print("\n" + SEPARATOR * 50)

        case "6":
            
            if loaded_numbers:
                while True:
                    try:
                        print("\n" + SEPARATOR * 70)
                        number_search_index = int(input("\nIngrese un numero para buscar si esta en la lista > ").strip())
                        while not number_search_index:
                            print("\n" + SEPARATOR * 70)
                            number_search_index = int(input("\n¡Error! Debe ingresar caracteres numéricos"
                                                        "mayores a 0 > ").strip())
                    
                        break
                    except ValueError:
                        print("\n" + SEPARATOR * 80)
                        print("\n¡Error! Debe ingresar caracteres numéricos mayores a 0, vuelva a intentarlo.")
                        continue

                print("\n" + SEPARATOR * 50)

                list_index = []

                for i in range(len(list_numbers)):
                    if list_numbers[i] == number_search_index:
                        list_index.append(i)

                if len(list_index) > 0:  
                    print(f"\nEl indice del numero {number_search_index} es: ")

                    for index in list_index:
                        print(index, end=' | ')
                    print()
                else:
                    print("\nEl numero ingresado no se encuentra en la lista.")

                print("\n" + SEPARATOR * 50)

            else:
                print("\n" + SEPARATOR * 50)
                print("\nPrimero debe ingresar los números.")
                print("\n" + SEPARATOR * 50)

        case "7":
            
            if loaded_numbers:
                list_numbers.clear()
                loaded_numbers = False

                print("\n" + SEPARATOR * 50)
                print("\nSe ha vaciado la lista.")
                print("\n" + SEPARATOR * 50)
            else:
                print("\n" + SEPARATOR * 50)
                print("\nPrimero debe ingresar los números.")
                print("\n" + SEPARATOR * 50)

        case "0":
            break
        case _:
            print("\n" + SEPARATOR * 50)
            print("\nOpción no valida, vuelva a intentarlo.")
            print("\n" + SEPARATOR * 50)

    input("\nPresione Enter para continuar...")