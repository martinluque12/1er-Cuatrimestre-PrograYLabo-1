import os
import platform
from data import *

def clear_console() -> None:
    """Limpia la consola.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def generate_separator(character: str, quantity: int) -> str:
    """Genera un separador de la longitud indicada con el carácter dado.

    Args:
        character (str): Carácter que va ser el separador.
        cantidad (int): La cantidad de veces a repetir el carácter.

    Returns:
        str: El separador.
    """
    if (isinstance(character, str) and isinstance(quantity, int)):
        return character * quantity


def validate_list_value(lista: list, value: str) -> bool:
    """Valida que una lista se de tipo lista y que no sea una lista vacía y que una clave sea de tipo string.

    Args:
        lista (list): La lista a validar.
        value (str): La clave a validar.

    Returns:
        bool: True si son del tipo que se espera, False de lo contrario.
    """
    if isinstance(lista, list) and len(lista) > 0 and isinstance(value, str):
        return True
    else:
        return False


def validate_if_it_is(dictionary: dict, element: str) -> bool:
    """Valida si un elemento se encuentra en un diccionario.

    Args:
        dictionary (dict): El diccionario en el cual se va a buscar el elemento.
        element (str): El elemento a buscar.

    Returns:
        bool: True si se encuentra en el diccionario.
    """
    if isinstance(dictionary, dict) and isinstance(element, str):

        for item in dictionary:
            if item == element:
                return True


def list_elements(lista: list, key: str, value: str) -> list:
    """Recorre una lista de diccionarios y guarda los elementos que coincidan con la clave y el valor
       que se pase por parámetro

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave del diccionario, en la que se quiere filtrar.
        value (str): El valor especifico de la clave del diccionario.

    Returns:
        list: Una lista de diccionarios con los elementos que se filtraron.
    """
    if validate_list_value(lista, key) and isinstance(value, str):
        
        list_elements = []

        for element in lista:
            if element[key] == value:
                list_elements.append(element)
        
        return list_elements


def calculate_largest_element(lista: list, key: str) -> list:
    """Calcula el/los elemento/s mas grande de una lista de diccionarios en la clave especificada 
       (solo claves que se puedan castear a float)

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave por la que se quiere buscar.

    Returns:
        list: Una lista de diccionarios con los elementos que sean mas grandes.
    """
    if validate_list_value(lista, key):

        largest_element = lista[0]
        largest_elements = []

        for element in lista:
            if float(element[key]) > float(largest_element[key]):
                largest_element = element

        for element in lista:
            if float(element[key]) == float(largest_element[key]):
                largest_elements.append(element)

        return largest_elements

 
def calculate_smallest_element(lista: list, key: str) -> list:
    """Calcula el/los elemento/s mas chico de una lista de diccionarios en la clave especificada 
       (solo claves que se puedan castear a float)

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave por la que se quiere buscar.

    Returns:
        list: Una lista de diccionarios con los elementos que sean mas chicos.
    """
    if validate_list_value(lista, key):
        
        smallest_element = lista[0]
        smallest_elements = []

        for element in lista:
            if float(element[key]) < float(smallest_element[key]):
                smallest_element = element

        for element in lista:
            if float(element[key]) == float(smallest_element[key]):
                smallest_elements.append(element)

        return smallest_elements


def calculate_average(lista: list, key: str) -> float:
    """Calcula un promedio, de una lista de diccionarios en la clave que se especifique.

    Args:
        lista (list): La lista de diccionarios.

    Returns:
        float: El promedio.
    """
    if validate_list_value(lista, key):

        average = 0

        for element in lista:
            average += float(element[key])

        return average / len(lista)


def calculate_quantity_type(lista: list, key: str) -> dict:
    """Calcula la cantidad de cada tipo para una clave específica en una lista de diccionarios.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave del diccionario en la cual se va a contabilizar.

    Returns:
        dict: Un diccionario que contiene el conteo de cada tipo para la clave especificada. 
    """
    if validate_list_value(lista, key):

        types = {}

        for element in lista:
            type = element[key]
            if type == "":
                type  = "no tiene"
            types[type.capitalize()] = 0

        for element in lista:
            type = element[key]
            if type == "":
                type  = "no tiene"
            types[type.capitalize()] += 1

        return types
            

def list_element_type(lista: list, key: str, value_show: str) -> dict:
    """Agrupa elementos que compartan el mismo valor de una clave especifica.

    Args:
        lista (list): Lista de diccionarios.
        key (str): La clave especifica.
        value_show (str): La clave que se va a guardar de los elementos.

    Returns:
        dict: Un diccionario que cada clave sea el valor de la clave que se especifico
        y el valor sea una lista con los elementos que comparten dicho valor.
    """
    if validate_list_value(lista, key) and isinstance(value_show, str):

        dict_types = {}

        for element in lista:
            value = element[key]
            if value == "":
                value = "No tiene"
            elif value == "blue":
                value = "Blue"
            if not validate_if_it_is(dict_types, value):
                dict_types[value] = []
            
            dict_types[value].append(element[value_show])

        return dict_types


def print_list_console(lista: list, key: str, key_show: str) -> None:
    """Imprime una lista de diccionarios por consola.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave que se va a mostrar en el primer print.
        key_show (str): La clave que se quiere mostrar el valor de cada elemento de la lista.
    """
    if validate_list_value(lista, key) and isinstance(key_show, str):
        
        print(f"\nLista filtrada por {key.capitalize()}\n")
        
        print(generate_separator("*", 40))

        for element in lista:
            print(element[key_show])
                
        print(generate_separator("*", 40))


def print_hero_largest(lista: list, gender: str) -> None:
    """Imprime por consola el/los heroes mas altos.

    Args:
        lista (list): La lista de diccionarios que necesita la función "calculate_largest_element()".
        gender (str): El genero del Héroe que se va a mostrar.
    """
    if validate_list_value(lista, gender):

        tallest_hero = calculate_largest_element(lista, "altura")

        print(generate_separator("*", 60))
        print(f"Los Heroes de genero {gender} mas altos son: \n")

        for hero in tallest_hero:
            print(f"{hero['nombre']} | {float(hero['altura']):.2f}cm")

        print(generate_separator("*", 60))


def print_hero_smallest(lista: list, gender: str) -> None:
    """Imprime por consola el/los heroes mas bajos.

    Args:
        lista (list): La lista de diccionarios que necesita la función "calculate_smallest_element()".
        gender (str): El genero del Héroe que se va a mostrar.
    """
    if validate_list_value(lista, gender):

        tallest_hero = calculate_smallest_element(lista, "altura")

        print(generate_separator("*", 60))
        print(f"Los Heroes de genero {gender} mas bajos son: \n")

        for hero in tallest_hero:
            print(f"{hero['nombre']} | {float(hero['altura']):.2f}cm")

        print(generate_separator("*", 60))


def print_average(lista: list, key: str, gender: str) -> None:
    """Imprime por consola un promedio.

    Args:
        lista (list): Lista de diccionarios que necesita la función "calculate_average()"
        key (str): Clave del diccionario que necesita la función "calculate_average()"
        gender (str): El genero de Heroes que se va a mostrar.
    """
    if validate_list_value(lista, key) and isinstance(gender, str):
        average = calculate_average(lista, key)
        
        print(generate_separator("*", 70))
        print(f"El promedio de altura de los Heroes de genero {gender} es: {average:.2f}cm")
        print(generate_separator("*", 70))   


def print_quantity_type(lista: list, key: str, type: str) -> None:
    """Imprime por consola la cantidad de elemento según la clave especificada.

    Args:
        lista (list): Lista de diccionario que necesita la funciones "calculate_quantity_type()".
        key (str): Clave del diccionario que necesita la funciones "calculate_quantity_type()".
        type (str): El tipo que se va a mostrar.
    """
    if validate_list_value(lista, key) and isinstance(type, str):

        dict = calculate_quantity_type(lista, key)

        print(f"\nCantidad de heroes por {type}:\n")
        print(generate_separator("=", 50))

        for value, quantity in dict.items():
            print(f"{value:<24} | Cantidad: {quantity}")

        print(generate_separator("=", 50))


def print_list_type(lista: list, key: str, type: str) -> None:
    """Imprime por consola los nombre de los Heroes agrupados por la clave que se especifique.

    Args:
        lista (list): Lista de diccionarios que necesita la función "list_element_type()".
        key (str): Clave del diccionario que necesita la función "list_element_type()".
        type (str): El tipo que se va a mostrar.
    """
    if validate_list_value(lista, key) and isinstance(type, str):

        list_type = list_element_type(lista, key, "nombre")
        print(f"\nHeroes agrupados por {type}.")
        for element, value in list_type.items():
            print(generate_separator("=", 25))
            print(element.capitalize() + ":")
            
            for item in value:
                print(item)


def confirm_exit() -> bool:
    """Pregunta si quiere salir de la app.

    Returns:
        bool: True si la respuesta es "si".
    """
    answer = input('\n¿Seguro que quiere salir de la APP? Responda con "si" o con "no" > ').lower()

    if answer == "si":
        return True


def menu() -> str:
    """
    El texto que se va a mostrar en el menu de la app.
    """
    menu = """\n                                       STARK APP

    A - Imprimir por consola los nombres de los Heroes de genero masculino.
    B - Imprimir por consola los nombres de los Heroes de genero femenino.
    C - Imprimir por consola el nombre y la altura del Héroe de genero masculino mas alto. 
    D - Imprimir por consola el nombre y la altura del Héroe de genero femenino mas alto. 
    E - Imprimir por consola el nombre y la altura del Héroe de genero masculino mas bajo. 
    F - Imprimir por consola el nombre y la altura del Héroe de genero femenino mas bajo. 
    G - Imprimir por consola el promedio de altura de los Heroes de genero masculino.
    H - Imprimir por consola el promedio de altura de los Heroes de genero femenino.
    I - Imprimir por consola la cantidad de Heroes por color de ojos.
    J - Imprimir por consola la cantidad de Heroes por color de pelo.
    K - Imprimir por consola la cantidad de Heroes por inteligencia.
    L - Agrupar e imprimir por consola los nombres de los heroes por color de ojos.
    M - Agrupar e imprimir por consola los nombres de los heroes por color de pelo.
    N - Agrupar e imprimir por consola los nombres de los heroes por inteligencia.
    Z - Salir.
    """
    
    return menu


def app_stark(lista: list) -> None:

    if validate_list_value(lista, ""):

        while True:

            clear_console()

            menu_app = input(menu() + "\n\n    > ").upper()

            match menu_app:

                case "A":
                    male_list = list_elements(lista, "genero", "M")
                    print_list_console(male_list, "genero", "nombre")
                case "B":
                    female_list = list_elements(lista, "genero", "F")
                    print_list_console(female_list, "genero", "nombre")
                case "C":
                    print_hero_largest(list_elements(lista, "genero", "M"), "Masculino")
                case "D":
                    print_hero_largest(list_elements(lista, "genero", "F"), "Femenino")
                case "E":
                    print_hero_smallest(list_elements(lista, "genero", "M"), "Masculino")
                case "F":
                    print_hero_smallest(list_elements(lista, "genero", "F"), "Femenino")
                case "G":
                    print_average(list_elements(lista, "genero", "M"), "altura", "Masculino")
                case "H":
                    print_average(list_elements(lista, "genero", "F"), "altura", "Femenino")
                case "I":
                    print_quantity_type(lista, "color_ojos", "color de ojos")
                case "J":
                    print_quantity_type(lista, "color_pelo", "color de pelo")
                case "K":
                    print_quantity_type(lista, "inteligencia", "inteligencia")
                case "L":
                    print_list_type(lista, "color_ojos", "color de ojos")
                case "M":
                    print_list_type(lista, "color_pelo", "color de pelo")
                case "N":
                    print_list_type(lista, "inteligencia", "inteligencias")
                case "Z":
                    if confirm_exit():
                        break
                case _:
                    print("\n¡Error! Opción no valida, vuelva a intentarlo.")
            
            input("\nPresione Enter para continuar...")
