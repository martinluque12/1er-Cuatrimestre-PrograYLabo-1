import os
import platform

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


def extract_initials(string: str) -> str:
    """Extrae las iniciales de un string, si contiene el articulo "the" lo elimina y si contiene un "-",
       lo reemplaza por un espacio en blanco.

    Args:
        string (str): El string del cual se van a extraer las iniciales.

    Returns:
        str: Un string con las iniciales unidas por ".", ej: "M.L."
    """
    if validate_string(string):

        string = string.upper()
        string = string.replace("THE", "")
        string = string.replace("-", " ").strip()
        separated_string = string.split(" ")

        initials = []

        for string in separated_string:
            if len(string) > 0:
                initials.append(string[0])

        initials = "".join(initial + "." for initial in initials)

        return initials

    else:
        return "N/A"


def define_initials_name(dictionary: dict) -> bool:
    """Agrega la clave "iniciales" a un diccionario que contenga la clave "nombre", con el valor 
       de las iniciales del nombre.

    Args:
        dictionary (dict): El diccionario al cual se le agregara la nueva clave.

    Returns:
        bool: True si se pudo agregar la clave al diccionario, False de lo contrario.
    """
    if validate_dict(dictionary) and "nombre" in dictionary:

        initials = extract_initials(dictionary["nombre"])

        dictionary["iniciales"] = initials

        return True
    
    else:
        return False
    

def add_initials_name(lista: list) -> bool:
    """Agrega la clave iniciales a los diccionarios contenidos en la lista, con el valor
       de las iniciales del valor de la clave "nombre", mediante la función "define_initials_name()"

    Args:
        lista (list): La lista de diccionarios.

    Returns:
        bool: True si se agrego la nueva clave a todos los diccionarios, False de lo contrario.
    """
    retorno = False

    if validate_list(lista):

        for item in lista:
            if define_initials_name(item):
                retorno = True
            else:
                print("El origen de datos no contiene el formato correcto")
                retorno = False
    
    return retorno
    

def stark_print_names_with_initials(lista: list) -> None:
    """Imprime por consola el valor de la clave "nombre" e "iniciales" de los diccionarios contenidos 
       en la lista.

    Args:
        lista (list): La lista de diccionarios.
    """
    if validate_list(lista):

        if add_initials_name(lista):

            for item in lista:
                print(f"* {item['nombre']} ({item['iniciales']})")


def generate_hero_code(id_hero: int, hero_gender: str) -> str:
    """Genera un código mediante un id y un genero (El genero debe estar entre estos valores : "M", "F" o "NB").

    Args:
        id_hero (int): Un dato numérico que representa el id.
        hero_gender (str): Un genero.

    Returns:
        str: El código en str formado por el id y el genero, ej de salida: "M-00000001", o "N/A"
             en caso de algún error
    """
    retorno = "N/A"

    if (isinstance(id_hero, int) and validate_string(hero_gender) and
       (hero_gender == "M" or hero_gender == "F" or hero_gender == "NB")):
        
        if hero_gender == "NB" and len(str(id_hero)) == 2:

            code = hero_gender + "-".zfill(6) + str(id_hero)

            retorno = code
        
        elif hero_gender == "NB" and len(str(id_hero)) == 1:

            code = hero_gender + "-".zfill(7) + str(id_hero)

            retorno = code
        
        elif (hero_gender == "F" or hero_gender == "M") and len(str(id_hero)) == 2:

            code = hero_gender + "-".zfill(7) + str(id_hero)

            retorno = code
        
        elif (hero_gender == "F" or hero_gender == "M") and len(str(id_hero)) == 1:

            code = hero_gender + "-".zfill(8) + str(id_hero)

            retorno = code
        
        else:
            
            retorno = "N/A"

        return retorno
        

def add_hero_code(dictionary: dict, id_hero: int) -> bool:
    """Agrega la clave "codigo_heroe" a un diccionario.

    Args:
        dictionary (dict): El diccionario a cual se le agregara la clave.
        id_hero (int): El id del diccionario.

    Returns:
        bool: True, si se agrego la clave, False de lo contrario.
    """
    retorno = False

    if validate_dict(dictionary) and len(str(id_hero)) == 10:

        dictionary["codigo_heroe"] = id_hero  

        retorno = True

    return retorno
 

def stark_generate_heroes_codes(lista: list) -> None:
    """Agrega la clave "codigo_heroe" a los diccionarios contenidos en la lista 
       e informa por pantalla si se pudo o no agregar la clave.

    Args:
        lista (list): La lista de diccionarios.
    """
    if (validate_list(lista) and all("genero" in item and item for item in lista)):

        print(f"Se generaron {len(lista)} códigos:\n")

        for index, dictionary in enumerate(lista, start=1):
            add_hero_code(dictionary, generate_hero_code(index, dictionary["genero"]))
            print(f"Código del {index}° Héroe: {dictionary['codigo_heroe']}")

    else:
        print("El origen de datos no contiene el formato correcto.")
            

def sanitize_int(number_str: str) -> int:
    """Verifica que un numero que es de tipo str, solo contenga números positivos y lo castea a int.

    Args:
        number_str (str): El numero a castear.

    Returns:
        int: Si pasa la validaciones retorna el numero casteado a int, si contiene letras retorna -1,
             si es un numero negativo retorna -2, si ocurre cualquier otro error retorna -3.
    """
    if validate_string(number_str):
        number_str = number_str.strip()

        try:
            number = int(number_str)

            if number < 0:
                retorno = -2
            else:
                retorno = number

        except(ValueError):
            retorno = -1
        
        except:
            retorno = -3

    else:
        retorno = -4

    return retorno


def sanitize_float(number_str: str) -> int | float:
    """Verifica que un numero que es de tipo str, solo contenga números positivos y lo castea a float.

    Args:
        number_str (str): El numero a castear.

    Returns:
        int | float: Si pasa la validaciones retorna el numero casteado a float, si contiene letras retorna -1,
                     si es un numero negativo retorna -2, si ocurre cualquier otro error retorna -3.
    """
    if validate_string(number_str):
        number_str = number_str.strip()

        try:
            number = float(number_str)

            if number < 0:
                retorno = -2
            else:
                retorno = number

        except(ValueError):
            retorno = -1
        
        except:
            retorno = -3

    else:
        retorno = -4

    return retorno


def sanitize_string(value_str: str, default_value: str="-") -> str:
    """Verifica que un string solo contenga caracteres alfanuméricos, si contiene un "/" lo reemplaza por " ".

    Args:
        value_str (str): El string a validar.
        default_value (str, optional): Parámetro por defecto. Defaults to "-".

    Returns:
        str: Retorna "N/A" si la cadena contiene números, retornara el string en minúscula si contiene solo
             caracteres numéricos, si no se pasan parámetros retornara el parámetro por defecto.
    """
    value_str = value_str.strip()
    value_str = value_str.replace("/", " ")

    if value_str.isdigit():
        retorno = "N/A"
    else:
        retorno = value_str.lower()

    if not value_str:
        retorno = default_value

    return retorno


def sanitize_data(dictionary: dict, key: str, type_data: str) -> bool:
    """Sanitiza el valor de una clave de un diccionario, dependiendo del tipo que se pase por parámetro.

    Args:
        dictionary (dict): El diccionario al cual se le sanitizaran la/las clave/s.
        key (str): La clave a sanitizar.
        type_data (str): El tipo de dato, puede ser "entero", "flotante" o "string".

    Returns:
        bool: True si se sanitizo aunque sea un dato, False de lo contrario.
    """
    if not validate_dict(dictionary) or not validate_string(key) or not validate_string(type_data):

        retorno = False
    
    elif not key in dictionary:

        print("La clave especificada no se existe en el Héroe.")

        retorno = False
    
    elif not type_data.lower() in ["entero", "flotante", "string"]:

        print("\nTipo de dato no reconocido.")

        retorno = False

    else:
        if type_data.lower() == "entero":
            dictionary[key] = sanitize_int(dictionary[key])
        elif type_data.lower() == "flotante":
            dictionary[key] = sanitize_float(dictionary[key])
        else:
            dictionary[key] = sanitize_string(dictionary[key])

        retorno = True

    return retorno


def stark_normalize_data(lista: list) -> None:
    """Normaliza las claves de un diccionario contenido en la lista.

    Args:
        lista (list): La lista de diccionarios.
    """
    if validate_list(lista):

        for item in lista:
            sanitize_data(item, "altura", "flotante")
            sanitize_data(item, "peso", "flotante")
            sanitize_data(item, "fuerza", "entero")
            sanitize_data(item, "color_pelo", "string")
            sanitize_data(item, "color_ojos", "string")
            sanitize_data(item, "inteligencia", "string")
         
        print("\nDatos normalizados.")

    else:
        print("\n¡Error! Lista vacía.")


def generate_name_indices(lista: list) -> list | None:
    """Divide el valor de la clave "nombre" de los diccionarios que están en la lista y los agrega a una lista.

    Args:
        lista (list): La lista de diccionarios.

    Returns:
        list | None: La lista con todos los nombres o imprime por consola si hubo algún error.
    """
    if validate_list(lista) and all("nombre" in item and isinstance(item, dict) and item for item in lista):
        
        names = []

        for item in lista:
            separated_name = item["nombre"].split(" ")
            names.extend(separated_name)

        return names
    else:
        print("\nEl origen de datos no contiene el formato correcto.")


def stark_print_name_index(lista: list) -> None:
    """Imprime por consola la lista de los nombres, generada por la función generate_name_indices(),
       uno al lado del otro separado por un "-".

    Args:
        lista (list): La lista con los nombres.
    """
    index = "-".join(generate_name_indices(lista))

    print(index)
    

def convert_cm_to_m(value_cm: float) -> float | int:
    """Convierte centímetros a metros.

    Args:
        value_cm (float): El valor en centímetros.

    Returns:
        float | int: El valor en metros, o -1 si no pasa la validación.
    """
    if isinstance(value_cm, float) and value_cm > 0:

        value_m = value_cm / 100

        return value_m
        
    else:
        return -1
    

def generate_header(title: str) -> str:
    """Genera un encabezado formado por la función generate_separator().

    Args:
        title (str): El titulo que se quiere mostrar en el encabezado.

    Returns:
        str: El encabezado en str.
    """
    if validate_string(title):

        header = f"{generate_separator('*', 140, False)}"
        header += f"\n{title.upper()}\n" 
        header += f"{generate_separator('*', 140, False)}"  
        
        return header


def print_hero_card(dictionary: dict) -> None:
    """Imprime una ficha con los datos de un diccionario.

    Args:
        dictionary (dict): El diccionario que representa 1 Héroe.
    """
    if validate_dict(dictionary):

        card = f"{generate_header('principal')}\n"
        card += f"""
        NOMBRE DEL HÉROE:                       {dictionary["nombre"]}
        IDENTIDAD SECRETA:                      {dictionary["identidad"]}
        CONSULTORA:                             {dictionary["empresa"]}
        CÓDIGO DE HÉROE :                       {dictionary["codigo_heroe"]}
        """
        card += f"\n{generate_header('físico')}\n"
        card += f"""
        ALTURA:                                 {dictionary["altura"]} cm  
        PESO:                                   {dictionary["peso"]} kg
        FUERZA:                                 {dictionary["fuerza"]}  
        """
        card += f"\n{generate_header('señas particulares')}\n"
        card += f"""
        COLOR DE OJOS:                          {dictionary["color_ojos"].capitalize()}
        COLOR DE PELO:                          {dictionary["color_pelo"].capitalize()}
        """

        print(card)


def stark_browse_tabs(lista: list) -> None:
    """Navega por las fichas de la lista de diccionarios, si el usuario ingresa "1", 
       se muestra la ficha a la izquierda, si ingresa "2" se muestra la ficha a la derecha,
       si ingresa "S" se vuelve al menu principal.

    Args:
        lista (list): La lista de diccionarios.
    """
    if validate_list(lista):

        current_index = 0

        while True:
            clear_screen()

            print_hero_card(lista[current_index])

            answer = input('\n[ 1 ] Ir a la izquierda.' +
                           '\n[ 2 ] Ir a la derecha.' +
                           '\n[ S ] Salir.\n> ').lower()
            
            if answer == "1":
                current_index -= 1
                if current_index < 0:
                    current_index = len(lista) - 1
            elif answer == "2":
                current_index += 1
                if current_index >= len(lista):
                    current_index = 0
            elif answer == "s":
                break


def print_menu() -> None:
    """Imprime por consola el menu de la app.
    """
    menu = """

    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Generar códigos de héroes
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    S - Salir

    ____________________________________________________________

    """

    print(menu)


def stark_main_menu() -> str:
    """Imprime el menu de opciones llamando a la función print_menu(), 
       y le pide al usuario que ingrese una opción.

    Returns:
        str: La respuesta del usuario.
    """
    print_menu()

    answer = input("> ")

    return answer


def stark_marvel_app(lista: list) -> None:
    """Función principal de la app.

    Args:
        lista (list): La lista de diccionarios.
    """
    if validate_list(lista):

        generated_codes = False
        normalized_data = False

        while True:

            clear_screen()
            option = stark_main_menu()

            match option:
                case "1":
                    generate_separator("*", 30)
                    stark_print_names_with_initials(lista)
                    generate_separator("*", 30)
                case "2":
                    if not generated_codes:
                        generate_separator("*", 40)
                        stark_generate_heroes_codes(lista)
                        generate_separator("*", 40)
                        generated_codes = True
                    else:
                        print("\nYa se han generado los códigos.")
                case "3":
                    if not normalized_data:
                        stark_normalize_data(lista)
                        normalized_data = True
                    else:
                        print("\nYa se han normalizado los datos.")
                case "4":
                    stark_print_name_index(lista)
                case "5":
                    if generated_codes and normalized_data:
                        stark_browse_tabs(lista)
                    else:
                        print("\nPrimero debe generar los códigos y normalizar los datos.")
                case "s":
                    answer = input('\n¿Seguro que quiere salir de la app? Responda con "si" o con "no" > ').lower()
                    if answer == "si":
                        break
                    else:
                        continue
                case _:
                    print("\n¡Error! Opción no valida.")

            input("\nPresione Enter para continuar...")
