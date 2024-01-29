import re

def validate_str(string: str) -> bool:
    """Valida que una variable sea de tipo str y que no este vacía.

    Args:
        string (str): La variable a validar.

    Returns:
        bool: True si es de tipo str y no esta vacía, False de lo contrario.
    """
    if isinstance(string, str) and string:
        return True
    else:
        return False


def validate_int(number: str) -> bool:
    """Valida que una variable str contenga solo caracteres numéricos.

    Args:
        number (str): La variable a validar.

    Returns:
        bool: True si la variable solo contiene caracteres numéricos, False de lo contrario.
    """
    if isinstance(number, str):
       
        pattern = re.compile(r'^[+-]?\d+$')
        if pattern.match(number):
            return True
        else:
            return False
    else:
        return False


def validate_float(number: str) -> bool:
    """Valida que una variable de tipo str sea de tipo float.

    Args:
        number (str): La variable a validar.

    Returns:
        bool: True si es un numero flotante, False de lo contrario.
    """
    if isinstance(number, str):
       
        pattern = re.compile(r'^[+-]?\d+(\.\d+)+$')
        if pattern.match(number):
            return True
        else:
            return False
    else:
        return False
    

def validate_list(data_list: list) -> bool:
    """Valida que una variable sea de tipo list y que no este vacía.

    Args:
        data_list (list): La variable a validar.

    Returns:
        bool: True si es de tipo lista y no esta vacía, False de lo contrario.
    """
    if isinstance(data_list, list) and data_list:
        return True
    else:
        return False
    

def validate_dict(dictionary: dict) -> bool:
    """Valida que una variable sea de tipo dict y que no este vacío.

    Args:
        dictionary (dict): La variable a validar.

    Returns:
        bool: True si es de tipo dict, False de lo contrario.
    """
    if isinstance(dictionary, dict) and dictionary:
        return True
    else:
        return False
    

def validate_key_in_dict(dictionary: dict, key: str) -> bool:
    """Valida que una clave se encuentre en un diccionario.

    Args:
        dictionary (dict): El diccionario donde buscar la clave.
        key (str): La calve a buscar en el diccionario.

    Returns:
        _type_: True si la calve se encuentra en el diccionario, False de l contrario.
    """
    if validate_dict(dictionary) and validate_str(key):

        for  k in dictionary.keys():
            if k.lower() == key.lower():
                return True
            
        return False
    else:
        return False