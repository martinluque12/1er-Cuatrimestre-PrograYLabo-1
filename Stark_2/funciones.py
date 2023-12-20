import os
import platform

def clear_screen()-> None:
    """Limpia la consola.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def generate_separator(pattern: str, long: int)-> None | int:
    """Imprime por consola un string que se utilizara como separador.

    Args:
        pattern (str): El carácter que se va a mostrar en el separador.
        long (int): El largo del separador.

    Returns:
        None | int: Si el patron pasado por parámetro es mas de 1 carácter y el largo no es de tipo int
                    o es menor a 0 o mayor a 236 retorna -1.        
    """
    if len(pattern) == 1 and isinstance(long, int) and long > 0 or long < 236:
        print_data(pattern * long)
    else:
        return -1


def validate_string(string: str) -> bool:
    """Valida que un string sea de tipo str.

    Args:
        string (str): String a validar.

    Returns:
        bool: True si es de tipo str, False de lo contrario.
    """
    if isinstance(string, str):
        return True
    else:
        return False


def validate_list(lista: list) -> bool:
    """Valida que una lista sea de tipo list y que no este vacía.

    Args:
        lista (list): La lista a validar.

    Returns:
        bool: True si la lista es de tipo list y no esta vacía, False de lo contrario.
    """
    if isinstance(lista, list) and len(lista) > 0:
        return True
    else:
        return False


def validate_dict(dictionary: dict) -> bool:
    """Valida que un diccionario sea de tipo dict.

    Args:
        dictionary (dict): El diccionario a validar.

    Returns:
        bool: True si el diccionario es de tipo dict, False de lo contrario.
    """
    if isinstance(dictionary, dict):
        return True
    else:
        return False
        

def print_data(message: str) -> None:
    """Imprime un mensaje por consola.

    Args:
        message (str): El mensaje a imprimir.
    """
    if validate_string(message):

        print(message)


def stark_normalize_data(lista: list) -> None:
    """Castea los valores de las key de una lista de diccionario al tipo correspondiente,
       si debe ser de tipo int o float.

    Args:
        lista (list): La lista de diccionarios.
    """
    if validate_list(lista):

        flag_casteo = False

        for dictionary in lista:
            for value in dictionary:
                if not isinstance(dictionary[value], (int, float)):
                    if dictionary[value].isdigit():
                        dictionary[value] = int(dictionary[value])

                        flag_casteo = True

                    elif "." in dictionary[value]:
                        dictionary[value] = float(dictionary[value])

        if flag_casteo:
            print_data("Datos normalizados.")

    else:
        print_data("\n¡Error! Lista vacía.")
            

def get_name(dictionary: dict) -> None:
    """Obtiene el valor de la clave "nombre" de un diccionario y lo imprime por consola mediante
       la función print_data().

    Args:
        dictionary (dict): El diccionario que contiene la clave "nombre".
    """
    if validate_dict(dictionary) and "nombre" in dictionary:
        name = dictionary["nombre"]

        print_data(f"Nombre: {name}")


def stark_print_hero_names(lista: list) -> None | int:
    """Imprime los nombres de los heroes que contiene la lista de diccionarios.

    Args:
        lista (list): Lista de diccionarios.

    Returns:
        None | int: No retorna nada, a menos que la lista no sea de tipo list o este vacía,
                    en ese caso retorna -1.
    """
    if validate_list(lista):

        for item in lista:
            get_name(item)
    else:
        return -1
    

def get_name_and_data(dictionary: dict, key: str) -> str:
    """Obtiene el valor de la clave "nombre" y de la key que se pase por parámetro de un diccionario.

    Args:
        dictionary (dict): El diccionario que contiene las claves y sus valores.
        key (str): La clave de la cual se quiere obtener su valor.

    Returns:
        str: Un string con los datos que se obtuvieron.
    """
    if validate_dict(dictionary) and "nombre" and key in dictionary and validate_string(key):

        return f"Nombre: {dictionary['nombre']:<20} | {key.capitalize()}: { dictionary[key]}"
        

def stark_print_names_heights(lista: list) -> None | int:
    """Imprime por consola el nombre y la altura de los diccionarios que contiene la lista.

    Args:
        lista (list): La lista de diccionarios.

    Returns:
        None | int: No retorna nada, a menos que la lista no sea de tipo list o este vacía,
                    en ese caso retorna -1.
    """
    if validate_list(lista):

        for item in lista:
            print_data(get_name_and_data(item, 'altura') + "cm")

    else:
        return -1
    

def calculate_max(lista: list, key: str) -> list:
    """Calcula el máximo de una lista de diccionarios, según la clave que se le pase por parámetro.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave por la cual se quiere calcular.

    Returns:
        list: Una lista con los diccionarios máximos.
    """
    if (validate_list(lista) and validate_string(key) and 
       (key == "altura" or key == "fuerza" or key == "peso")):

        list_max = []
        item_max = lista[0]

        for item in lista:
            if item[key] > item_max[key]:
                item_max = item

        for item in lista:
            if item[key] == item_max[key]:
                list_max.append(item)

        return list_max
    

def calculate_min(lista: list, key: str) -> list:
    """Calcula el mínimo de una lista de diccionarios, según la clave que se le pase por parámetro.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave por la cual se quiere calcular.

    Returns:
        list: Una lista con los diccionarios mínimos.
    """
    if (validate_list(lista) and validate_string(key) and 
       (key == "altura" or key == "fuerza" or key == "peso")):

        list_min = []
        item_min = lista[0]

        for item in lista:
            if item[key] < item_min[key]:
                item_min = item

        for item in lista:
            if item[key] == item_min[key]:
                list_min.append(item)

        return list_min
    

def calculate_max_min_data(lista: list, type_calculation: str, key: str) -> list:
    """Calcula máximo y mínimo de una lista de diccionarios según el tipo que se le pase por parámetro y 
       la clave que se le pase por parámetro, mediante las funciones calculate_max() y calculate_min()    

    Args:
        lista (list): La lista de diccionarios.
        type_calculation (str): El tipo de calculo, puede ser "max" o "min"
        key (str): La clave por la cual se quiere calcular.

    Returns:
        list: Una lista de diccionarios con los mínimos o los máximos.
    """
    if (validate_list(lista) and validate_string(type_calculation) and (type_calculation == "max" or type_calculation == "min") and
        validate_string(key)):

        if type_calculation == "max":
            return calculate_max(lista, key)
        elif type_calculation == "min":
            return calculate_min(lista, key)


def stark_calculate_print_hero(lista: list, type_calculation: str, key: str) -> None | int:
    """Imprime por consola los Heroes que sean máximos o mínimos en una clave especifica.

    Args:
        lista (list): La lista de Heroes.
        type_calculation (str): El tipo de calculo, puede ser "max" o "min"
        key (str): La clave por la que se quiere calcular.

    Returns:
        None | int: No retorna nada a menos que la lista no sea de tipo list o este vacía o 
                    el type_calculation no sea de tipo str o la key no sea de tipo str, en ese caso retorna -1.
    """
    if validate_list(lista) and validate_string(type_calculation) and validate_string(key):

        if type_calculation == "max":
            list_max = calculate_max_min_data(lista, "max", key)
            for item in list_max:
                print_data(f"Mayor {key.capitalize()}: Nombre: {item['nombre']} | {key.capitalize()}: {item[key]}")
        elif type_calculation == "min":
            list_max = calculate_max_min_data(lista, "min", key)
            for item in list_max:
                print_data(f"Menor {key.capitalize()}: Nombre: {item['nombre']} | {key.capitalize()}: {item[key]}")
    else:
        return -1
    

def sum_data_hero(lista: list, key: str) -> float:
    """Suma valores de una lista de diccionarios en la calve que se le pase por parámetro.

    Args:
        lista (list): L alista de diccionarios.
        key (str): La clave por la cual se quiere sumar.

    Returns:
        float: La suma total.
    """
    if validate_list(lista) and validate_string(key):

        total_sum = 0

        for item in lista:
            if isinstance(item, dict) and len(item) > 0:
                total_sum += item[key]

        return total_sum


def divide(dividend: float|int, divisor: float|int) -> float | int:
    """Divide 1 numero.

    Args:
        dividend (float | int): El dividendo puede ser un float o un int.
        divisor (float | int): El divisor puede ser un float o un int mayor a 0.

    Returns:
        float | int: El resultado de la division o 0 si el divisor es 0.
    """
    if isinstance(dividend, (float, int)) and isinstance(divisor, (float, int)) and divisor != 0:

        result = dividend / divisor

        return result
    else:
        return 0


def calculate_average(lista: list, key: str) -> float: 
    """Calcula el promedio de una lista de diccionarios, según la clave que se le pase por parámetro.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave en la cual se quiere calcular el promedio, puede ser "altura", "fuerza" o "peso".

    Returns:
        float: El promedio.
    """
    if (validate_list(lista) and validate_string(key) and 
       (key == "altura" or key == "fuerza" or key == "peso")):
        
        total_sum = sum_data_hero(lista, key)

        average = divide(total_sum, len(lista))

        return average


def stark_calculate_print_average_heights(lista: list) -> None | int:
    """Imprime por consola el promedio de alturas de Heroes de una lista de diccionarios.

    Args:
        lista (list): La lista de diccionarios.

    Returns:
        None | int: No retorna nada a menos que la lista no sea de tipo list, o este vacía,
                    en ese caso retorna -1.
    """
    if validate_list(lista):
        average = calculate_average(lista, "altura")
        print_data(f"Promedio de alturas: {average:.2f}cm")

    else:
        return -1


def print_menu() -> None:
    """
    Imprime por consola el menu de la app.
    """
    menu = """
    **Menu STARK INDUSTRIES**

    1- Normalizar datos.
    2- Imprimir nombre de los Superhéroes.
    3- Imprimir nombre y altura de los Superhéroes.
    4- Mostrar Superhéroe mas alto.
    5- Mostrar Superhéroe mas bajo.
    6- Mostrar promedio de altura de los Superhéroes.
    7- Mostrar Superhéroe mas y menos pesado (kg)
    0- Salir
    """

    print_data(menu)


def validate_int(integer: str) -> bool:
    """Valida que un numero ingresado sea un entero positivo.

    Args:
        integer (str): El numero a validar.

    Returns:
        bool: True si es un entero, False de lo contrario.
    """
    return integer.isdigit()


def stark_main_menu() -> int:
    """Imprime el menu en consola, mediante la función print_menu() y le pide al usuario que ingrese una opción.

    Returns:
        int: La opción ingresada o -1 en caso de que no se ingrese un numero.
    """
    print_menu()

    entered_number = input("Ingrese una opción > ")
    print()

    if validate_int(entered_number):
        return int(entered_number)
    else:
        return -1
    

def stark_marvel_app(lista: list) -> None:
    """Función principal de la app, muestra el contenido de la app, según la opción ingresada.

    Args:
        lista (list): La lista de diccionarios, donde se encuentra toda la data de los Heroes.
    """
    if validate_list(lista):

        flag_first_entry = False

        while True:

            clear_screen()
            option = stark_main_menu()

            match option:

                case 1:
                    if not flag_first_entry:
                        generate_separator("*", 20)
                        stark_normalize_data(lista)
                        generate_separator("*", 20)
                        flag_first_entry = True
                    else:
                        print("\nYa se normalizaron los datos.")
                case 2:
                    if flag_first_entry:
                        generate_separator("*", 30)
                        stark_print_hero_names(lista)
                        generate_separator("*", 30)
                    else:
                        print("\nPrimero debe normalizar los datos.")
                case 3:
                    if flag_first_entry:
                        generate_separator("*", 55)
                        stark_print_names_heights(lista)
                        generate_separator("*", 55)
                    else:
                        print("\nPrimero debe normalizar los datos.")
                case 4:
                    if flag_first_entry:
                        generate_separator("*", 50)
                        stark_calculate_print_hero(lista, "max", "altura")
                        generate_separator("*", 50)
                    else:
                        print("\nPrimero debe normalizar los datos.")
                case 5:
                    if flag_first_entry:
                        generate_separator("*", 55)
                        stark_calculate_print_hero(lista, "min", "altura")
                        generate_separator("*", 55)
                    else:
                        print("\nPrimero debe normalizar los datos.")
                case 6:
                    if flag_first_entry:
                        generate_separator("*", 30)
                        stark_calculate_print_average_heights(lista)
                        generate_separator("*", 30)
                    else:
                        print("\nPrimero debe normalizar los datos.")
                case 7:
                    if flag_first_entry:
                        generate_separator("*", 40)
                        stark_calculate_print_hero(lista, "max", "peso")
                        generate_separator("*", 40)
                        stark_calculate_print_hero(lista, "min", "peso")
                        generate_separator("*", 40)
                    else:
                        print("\nPrimero debe normalizar los datos.")
                case 0:
                    break
                case _:
                    print("\n¡Error! Opción invalida, vuelva a intentarlo.")


            input("\nPresione Enter para continuar...")