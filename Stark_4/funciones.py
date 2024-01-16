import os
import platform
import re
import json

def clear_screen() -> None:
    """Limpia la consola.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def generate_separator(pattern: str, long: int, imprimir: bool=True) -> None | str:
    """Genera un separador, conformado por el patron y el largo.

    Args:
        pattern (str): Uno o 2 caracteres, para formar el separador.
        long (int): El largo del separador que se desea.
        imprimir (bool, optional): Parámetro opcional, verifica si se debe imprimir o no. Defaults to True.

    Returns:
        None | str: Si el parámetro opcional se encentra en True, se imprime por consola el separador generado,
                    si no, solo se retorna el separador generado o si no pasa las validaciones se retornara "N/A".
    """
    if (validate_string(pattern) and len(pattern) == 1 or len(pattern) == 2 and
        isinstance(long, int) and long > 0 or long < 236):

        if imprimir:
            print(pattern * long)
        else:
            return pattern * long
    else:
        return "N/A"


def validate_string(string: str) -> bool:
    """Valida que un string sea de tipo str.

    Args:
        string (str): String a validar.

    Returns:
        bool: True si es de tipo str, False de lo contrario.
    """
    if isinstance(string, str) and len(string) > 0:
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


def print_menu() -> None:
    """Imprime el menu de la app en consola.
    """
    menu = """

    A - Imprimir los nombres de los Héroes masculinos.
    B - Imprimir los nombres de los Héroes femeninos.
    C - Determinar cual es el Héroe de genero masculino mas alto.
    D - Determinar cual es el Héroe de genero femenino mas alto.
    E - Determinar cual es el Héroe de genero masculino mas bajo.
    F - Determinar cual es el Héroe de genero femenino mas bajo.
    G - Calcular el promedio de alturas de los Héroes de genero masculino.
    H - Calcular el promedio de alturas de los Héroes de genero femenino.
    I - Calcular cuantos Héroes tiene cada tipo de color de ojos.
    J - Calcular cuantos Héroes tiene cada tipo de color de pelo.
    K - Calcular cuantos Héroes tiene cada tipo de inteligencia.
    L - Listar los Héroes por color de ojos.
    M - Listar los Héroes por color de pelo.
    N - Listar los Héroes por inteligencia.
    z - Salir.
    __________________________________________________________________________
    """

    print_data(menu)


def stark_main_menu() -> str | int:
    """Imprime el menu de opciones por consola mediante la función "print_menu()", le pide al usuario
       que ingrese una opción y valida que sea  una letra de la A a la Z (mayúscula o minúscula) mediante
       RegEx.

    Returns:
        str | int: Si el usuario ingresa una letra, retorna la letra, si ingresa cualquier otra cosa retorna -1.
    """
    print_menu()

    option = input("   > ")

    if re.search("^[a-z]$", option, re.IGNORECASE):
        return option
    else:
        return -1


def star_marvel_app(lista: list) -> None:
    """Función principal de la app, muestra el menu de opciones, pide al usuario una opción, dependiendo
       la opción ingresada por el usuario muestra diferentes cosas.

    Args:
        lista (list): La lista de diccionarios donde se encuentra la información para la ejecución del programa.
    """
    if validate_list(lista):

        while True:

            clear_screen()

            option = stark_main_menu()

            match option:

                case "a"|"A":
                    stark_save_hero_gender(lista, "M")
                case "b"|"B":
                    stark_save_hero_gender(lista, "F")
                case "c"|"C":
                    stark_calculate_print_save_hero_gender(lista, "max", "altura", "M")
                case "d"|"D":
                    stark_calculate_print_save_hero_gender(lista, "max", "altura", "F")
                case "e"|"E":
                    stark_calculate_print_save_hero_gender(lista, "min", "altura", "M")
                case "f"|"F":
                    stark_calculate_print_save_hero_gender(lista, "min", "altura", "F")
                case "g"|"G":
                    stark_calculate_print_save_average_heights_gender(lista, "M")
                case "h"|"H":
                    stark_calculate_print_save_average_heights_gender(lista, "F")
                case "i"|"I":
                    stark_calculate_quantity_for_type(lista, "color_ojos")
                case "j"|"J":
                    stark_calculate_quantity_for_type(lista, "color_pelo")
                case "k"|"K":
                    stark_calculate_quantity_for_type(lista, "inteligencia")
                case "l"|"L":
                    stark_list_heroes_by_data(lista, "color_ojos")
                case "m"|"M":
                    stark_list_heroes_by_data(lista, "color_pelo")
                case "n"|"N":
                    stark_list_heroes_by_data(lista, "inteligencia")
                case "z"|"Z":
                    break
                case _:
                    print("\nOpción no valida, vuelva a intentarlo.")
                    
            
            input("\nPresione Enter para continuar...")


def read_file(name_file: str) -> list:
    """Lee un archivo JSON y lo convierte en una lista de diccionarios.

    Args:
        name_file (str): Nombre del archivo con su extensión.

    Returns:
        list: El archivo JSON convertido en una lista de diccionarios.
    """
    if validate_string(name_file):

        with open (name_file, "r") as file:

            data = json.load(file)

            return data["heroes"]


def save_file(name_file: str, content: str) -> bool:
    """Guarda contenido (en string) en un archivo, si el archivo no existe lo crea, si existe lo sobrescribe.

    Args:
        name_file (str): El nombre que tendrá el archivo.
        content (str): El contenido del archivo.

    Returns:
        bool: True si se pudo crear el archivo, False de lo contrario.
    """
    if validate_string(name_file) and validate_string(content):
        
        file_path = os.path.join("Stark_4\File_csv", name_file)

        with open(file_path, "w+", encoding="utf-8") as file:
            file.write(content)

            print_data(f"\nSe creó el archivo: {file_path}")

            return True
    else:
        print_data(f"\nError al crear el archivo: {file_path}")
        return False

def capitalize_word(string: str) -> str:
    """Pone en mayúscula cada primer letra de una cadena de texto.

    Args:
        string (str): La cadena de texto.

    Returns:
        str: Retorna la cadena pero con cada primer letra en mayúscula.
    """
    if validate_string(string):

        string = string.strip()
        string = string.split(" ")
        string_capitalizado = []

        for word in string:
            word = word.capitalize()
            string_capitalizado.append(word)

        string_capitalizado = " ".join(word + "" for word in string_capitalizado)

        return string_capitalizado
            

def get_capitalized_name(dictionary: dict) -> str:
    """Capitaliza las primeras letras de un nombre contenido en un diccionario.

    Args:
        dictionary (dict): El diccionario que contiene el nombre.

    Returns:
        str: Un string formateado de la sig manera: "Nombre: {nombre capitalizado}"
    """
    if validate_dict(dictionary):

        return f"Nombre: {capitalize_word(dictionary['nombre'])}"


def get_name_and_data(dictionary: dict, key: str) -> str:
    """Genera un formato de cadena que incluye un nombre capitalizado y datos asociados a una clave

    Args:
        dictionary (dict): El diccionario que contiene el nombre.
        key (str): Clave del diccionario.

    Returns:
        str: Una cadena de texto formateada de la sig manera: 
             "Nombre: {nombre capitalizado} | {la clave}: {valor de la clave}.
    """
    if validate_dict(dictionary) and validate_string(key) and key in dictionary:

        return f"{get_capitalized_name(dictionary)} | {key.capitalize()}: {float(dictionary[key]):.2f}"


def is_gender(dictionary: dict, gender: str) -> bool:
    """Verifica si un diccionario en la clave "genero" es igual al genero que se le pasa por parámetro.

    Args:
        dictionary (dict): El diccionario a evaluar.
        gender (str): El genero que se quiere comparar.

    Returns:
        bool: True si el diccionario en la clave "genero" es igual al genero pasado por parámetro, 
              False de lo contrario.
    """
    if (validate_dict(dictionary) and validate_string(gender) and 
       (gender == "M" or gender == "F" or gender == "NB")):
        
        if dictionary["genero"] == gender:
            return True
        else:
            return False
        

def stark_save_hero_gender(lista: list, gender: str) -> bool:
    """Guarda en un archivo con extensión csv los heroes que tenga el genero pasado por parámetro mediante
       la función "save_file()", también imprime los nombres de los heroes por consola mediante la función
       "print_data()".

    Args:
        lista (list): La lista de diccionarios que contiene la info de los Heroes.
        gender (str): El genero del Héroe.

    Returns:
        bool: True si se pudo guardar los nombres en el archivo csv, False de lo contrario.
    """
    if validate_list(lista) and validate_string(gender) and (gender == "M" or gender == "F" or gender == "NB"):

        heroes_coincidentes = []

        for item in lista:
            if is_gender(item, gender):
                print_data(get_capitalized_name(item))
                heroes_coincidentes.append(capitalize_word(item["nombre"]))

        if heroes_coincidentes:
            contenido = ",".join(heroes_coincidentes)
            return save_file(f"heroes_{gender.upper()}.csv", contenido)
    
    return False

        
def calculate_min_gender(lista: list, key: str, gender: str) -> list:
    """Calcula el Héroe mínimo en la clave especificada de una lista de diccionarios según el genero
       que se le pase por parámetro.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave que se quiere calcular.
        gender (str): El genero del Héroe.

    Returns:
        list: Una lista con los diccionarios mínimos 
    """
    if(validate_list(lista) and validate_string(key) and validate_string(gender) and
      (gender == "M" or gender == "F" or gender == "NB")):
        
        flag_first_gender = False
        item_min = None
        list_min = []

        for item in lista:
            if not flag_first_gender and item["genero"] == gender:
                item_min = item
                flag_first_gender = True

            if item["genero"] == gender:
                if float(item[key]) < float(item_min[key]):
                    item_min = item

        for item in lista:
            if item["genero"] == gender:
                if float(item[key]) == float(item_min[key]):
                    list_min.append(item)

        return list_min
        

def calculate_max_gender(lista: list, key: str, gender: str) -> list:
    """Calcula el Héroe máximo en la clave especificada de una lista de diccionarios según el genero
       que se le pase por parámetro.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave que se quiere calcular.
        gender (str): El genero del Héroe.

    Returns:
        list: Una lista con los diccionarios máximos. 
    """
    if(validate_list(lista) and validate_string(key) and validate_string(gender) and
      (gender == "M" or gender == "F" or gender == "NB")):
        
        flag_first_gender = False
        item_max = None
        list_max = []

        for item in lista:
            if not flag_first_gender and item["genero"] == gender:
                item_max = item
                flag_first_gender = True

            if item["genero"] == gender:
                if float(item[key]) > float(item_max[key]):
                    item_max = item

        for item in lista:
            if item["genero"] == gender:
                if float(item[key]) == float(item_max[key]):
                    list_max.append(item)

        return list_max


def calculate_max_min_data_gender(lista: list, type_calculation: str, key: str, gender: str) -> list:
    """Calcula máximo y mínimo de una lista de diccionarios según el tipo que se le pase por parámetro y 
       la clave que se le pase por parámetro, mediante las funciones calculate_max_gender() y
       calculate_min_gender().

    Args:
        lista (list): La lista de diccionarios.
        type_calculation (str): El tipo de calculo, puede ser "max" o "min"
        key (str): La clave por la cual se quiere calcular.
        gender (str): El genero del Héroe a calcular.

    Returns:
        list: Una lista de diccionarios con los mínimos o los máximos.
    """
    if (validate_list(lista) and validate_string(type_calculation) and 
        (type_calculation == "max" or type_calculation == "min") and validate_string(key) and 
        validate_string(gender)):

        if type_calculation == "max":
            return calculate_max_gender(lista, key, gender)
        elif type_calculation == "min":
            return calculate_min_gender(lista, key, gender)


def stark_calculate_print_save_hero_gender(lista: list, type_calculation: str, key: str, gender: str) -> bool:
    """Realiza un cálculo, imprime y guarda en un archivo CSV el resultado para héroes de un género específico.

    Args:
        lista (list): La lista de diccionarios.
        type_calculation (str): El tipo de calculo, puede ser "max" o "min".
        key (str): La clave del diccionario a calcular.
        gender (str): El genero del Héroe de los cuales se quieren calcular.

    Returns:
        bool: True si se pudo guardar el archivo csv, False de lo contrario.
    """
    if validate_list(lista) and validate_string(type_calculation) and validate_string(key):

        if type_calculation == "max":
            list_max = calculate_max_min_data_gender(lista, "max", key, gender)
            for item in list_max:
                content_max = f"Mayor {key.capitalize()}: {get_name_and_data(item, key)}"
                print_data(content_max)
                if save_file(f"heroes_{type_calculation}_{key}_{gender}.csv", content_max):
                    return True
                else:
                    return False

        elif type_calculation == "min":
            list_max = calculate_max_min_data_gender(lista, "min", key, gender)
            for item in list_max:
                content_min = f"Menor {key.capitalize()}: {get_name_and_data(item, key)}"
                print_data(content_min)
                if save_file(f"heroes_{type_calculation}_{key}_{gender}.csv", content_min):
                    return True
                else:
                    return False
    

def sum_data_hero_gender(lista: list, key: str, gender: str) -> float | int:
    """Suma valores de una lista de diccionarios en la calve que se le pase por parámetro.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave por la cual se quiere sumar.
        gender (str) El genero sobre el cual se quiere calcular.

    Returns:
        float | int: La suma total o -1 en caso de que no pase la validación.
    """
    if validate_list(lista) and validate_string(key) and validate_string(gender):

        total_sum = 0

        for item in lista:
            if isinstance(item, dict) and len(item) > 0 and item["genero"] == gender:
                total_sum += float(item[key])
            
        return total_sum
    else:
        return -1


def quantity_heroes_gender(lista: list, gender: str) -> int:
    """Calcula la cantidad de Heroes por genero de una lista de diccionarios.

    Args:
        lista (list): La lista de diccionarios.
        gender (str): El genero que se quiere saber cuantos hay.

    Returns:
        int: La cantidad de Heroes según el genero pasado por parámetro.
    """
    if validate_list(lista) and validate_string(gender):

        quantity_gender = 0

        for item in lista:
            if item["genero"] == gender:
                quantity_gender += 1

        return quantity_gender


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
    

def calculate_average_gender(lista: list, key: str, gender: str) -> float: 
    """Calcula el promedio de una lista de diccionarios, según la clave que se le pase por parámetro y
       el genero pasado por parámetro.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave en la cual se quiere calcular el promedio, puede ser "altura", "fuerza" o "peso".
        gender (str): El genero de los Héroes de los cuales se quiere calcular el promedio.

    Returns:
        float: El promedio.
    """
    if (validate_list(lista) and validate_string(key) and 
       (key == "altura" or key == "fuerza" or key == "peso")):
        
        total_sum = sum_data_hero_gender(lista, key, gender)

        average = divide(total_sum, quantity_heroes_gender(lista, gender))

        return average
    

def stark_calculate_print_save_average_heights_gender(lista: list, gender: str) -> bool:
    """Imprime por consola el promedio de alturas de Heroes de una lista de diccionarios según el genero
       pasado por parámetro.

    Args:
        lista (list): La lista de diccionarios.
        gender (str): El genero de los Héroes que se quiere calcular el promedio de alturas.

    Returns:
        bool: True si se pudo guardar el archivo CSV, False de lo contrario.
    """
    if validate_list(lista) and validate_string(gender) and (gender == "M" or gender == "F"):

        average = calculate_average_gender(lista, "altura", gender)
        message_average = f"Altura promedio genero {gender}: {average:.2f}cm"
        print_data(message_average)
        if save_file(f"heroes_promedio_altura_{gender}.csv", message_average):
            return True
    else:
        print_data("\nError: Lista de héroes vacía")
        return False
    

def calculate_quantity_type(lista: list, key: str) -> dict:
    """Calcula la cantidad de una clave que se le pase por parámetro en una lista de diccionarios.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave que se quiere calcular la cantidad.

    Returns:
        dict: Un diccionario con clave que sera el valor de la calve pasada por parámetro y
        el valor sera la cantidad de ocurrencias o en caso de que no pase la validación un 
        diccionario con clave "Error" y valor "La lista se encuentra vacía.".
    """
    if validate_list(lista) and validate_string(key):

        quantities = {}

        for item in lista:
            quantity = item[key]
            if quantity == "":
                quantity  = "no tiene"
            quantities[capitalize_word(quantity)] = 0

        for item in lista:
            quantity = item[key]
            if quantity == "":
                quantity  = "no tiene"
            quantities[capitalize_word(quantity)] += 1
        
        return quantities
    else:
        return {"Error": "La lista se encuentra vacía."}
    

def save_quantity_heroes_type(dictionary: dict, date: str) -> bool:
    """Guarda la cantidad de héroes por cada característica en un archivo CSV y lo imprime por consola.

    Args:
        dictionary (dict): Un diccionario que representa las distintas variedades de una característica,
                           donde las claves son las variedades y los valores son las cantidades de héroes.
        date (str): El dato específico de la característica que se utilizará en el mensaje final.

    Returns:
        bool: True si se pudo guardar el archivo CSV, False de lo contrario.
    """
    if validate_dict(dictionary) and validate_string(date):
        file_name = f"heroes_cantidad_{date}.csv"
        content = ""

        for key, value in dictionary.items():
            feature = f"Características: {date} {key} - Cantidad de Heroes {str(value)}\n"
            content += feature

            print_data(feature)

        if save_file(file_name, content):
            return True
        else:
            return False
    else:
        return False


def stark_calculate_quantity_for_type(lista: list, key: str) -> bool:
    """Calcula la cantidad de una clave de una lista de diccionarios mediante la función "calculate_quantity_type()"
       y guarda la información en un archivo CSV.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave que se quiere calcular la cantidad.

    Returns:
        bool: True si se pudo guardar el archivo, False de lo contrario.
    """
    if validate_list(lista) and validate_string(key):

        dictionary = calculate_quantity_type(lista, key)

        if save_quantity_heroes_type(dictionary, key):
            return True
        else:
            return False
        

def get_list_of_types(lista: list, key: str) -> set:
    """Guarda en una set los valores de una clave de un diccionario contenido en una lista.

    Args:
        lista (list): La lista de diccionarios.
        key (str): La clave de la cual se quieren guardar los valores.

    Returns:
        set: Una set con los valores de la clave pasada por parámetro.
    """
    if validate_list(lista) and validate_string(key):
        
        set_types = set()

        for item in lista:
            types = capitalize_word(item[key])
            if types == None:
                types = "N/A"
            set_types.add(types)

        return set_types


def normalize_date(value_key: str, default_value: str) -> str:
    """Normaliza un dato, reemplazando el valor vacío con un valor por defecto. 

    Args:
        value_key (str): El valor a evaluar.
        default_value (str): El valor por defecto a colocar en caso de que el "value_key" esté vacío.

    Returns:
        str: El dato normalizado, reemplazando el valor vacío con el valor por defecto.
    """
    if validate_string(value_key):
        return capitalize_word(value_key)
    else:
        return default_value


def normalize_hero(dictionary: dict, key: str) -> dict:
    """Capitaliza el nombre contenido en un diccionario y el valor de una clave que se le pase por parámetro.

    Args:
        dictionary (dict): El diccionario que contiene el nombre y la clave.
        key (str): La clave que se quiere capitalizar.

    Returns:
        dict: Retorna el diccionario con el nombre y la clave capitalizada.
    """
    if validate_dict(dictionary) and validate_string(key) and key in dictionary:

        original_key = capitalize_word(dictionary[key])
        capitalize_key = normalize_date(original_key, "N/A")

        capitalize_name = capitalize_word(dictionary["nombre"])

        normalize_dict = {
            "nombre": capitalize_name,
            key: capitalize_key
        }

        return normalize_dict


def get_heroes_for_type(lista: list, types: set, key: str) -> dict:
    """Guarda en un diccionario como clave los valores de un set y como valor una lista vacía,
       recorre una lista de diccionarios y los items que coinciden la clave que se pasa como parámetro
       se guarda el valor de la clave "nombre" dentro de la lista que tiene como valor cada clave.

    Args:
        lista (list): La lista de diccionarios.
        types (set): El set con los tipos/variedades.
        key (str): La clave que se quiere evaluar.

    Returns:
        dict: Un diccionario que contiene tipos/variedades como claves y listas de nombres como valores.
    """
    if validate_list(lista) and isinstance(types, set) and validate_string(key):

        dict_types = {}

        for variants in types:
            if not variants in dict_types:
                dict_types[variants] = []

            for item in lista:
                key_normalize = normalize_date(item[key], "N/A")
                if key_normalize == variants:
                    dict_types[variants].append(item["nombre"])

        return dict_types
                

def save_heroes_for_type(dictionary: dict, key: str) -> bool:
    """Formatea un string formado por la clave que se quiere mostrar y los Heroes que tienen cada
       valor de la clave y lo guarda en un archivo CSV.

    Args:
        dictionary (dict): El diccionario que devuelve la función "get_heroes_for_type()".
        key (str): La clave que se quiere mostrar.

    Returns:
        bool: True si se pudo guardar en el archivo CSV, False de lo contrario.
    """
    if validate_dict(dictionary) and validate_string(key):

        file_name = f"heroes_segun_{key}.csv"
        content = ""
        
        for clave, value in dictionary.items():
            names = " | ".join(value)
            feature = f"{capitalize_word(key)} {clave} : {names}\n"
            content += feature

            print_data(feature)

        if save_file(file_name, content):
            return True
        else:
            return False


def stark_list_heroes_by_data(lista: list, key: str) -> bool:
    """Obtiene el set que retorna la función "get_list_of_types()", obtiene el diccionario que retorna 
       la función "get_heroes_for_type()" y guarda el resultado en un archivo CSV mediante la función
       "save_heroes_for_type()".

    Args:
        lista (list): La lista de diccionarios que contiene la data de los Heroes.
        key (str): La clave que se quiere guardar en el archivo CSV.

    Returns:
        bool: True si se pudo guardar el archivo CSV, False de lo contrario.
    """
    if validate_list(lista) and validate_string(key):

        set_types = get_list_of_types(lista, key)
        dictionary = get_heroes_for_type(lista, set_types, key)

        if save_heroes_for_type(dictionary, key):
            return True
        else:
            return False


