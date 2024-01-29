import re

def validate_str(string: str) -> bool:
    """Valida que una variable sea de tipo str y que no este vacía.

    Args:
        string (str): La variable a validar.

    Returns:
        bool: True si la variable es de tipo str, False de lo contrario.
    """
    if isinstance(string, str) and string:
        return True
    else:
        return False
    

def validate_int(number: str) -> bool:
    """Valida mediante RegEx que una variable de tipo str contenga solo caracteres numéricos enteros.

    Args:
        number (str): La variable a validar.

    Returns:
        bool: True si contiene solo caracteres numéricos enteros, False de lo contrario.
    """
    if validate_str(number):

        pattern = re.compile(r'^[+-]?\d+$')

        if pattern.match(number):
            return True
        else:
            return False
    else:
        return False
    

def validate_float(number: str) -> bool:
    """Valida mediante RegEx que una variable de tipo str solo contenga caracteres de punto flotante. 

    Args:
        number (str): La variable a validar.

    Returns:
        bool: True si contiene solo caracteres de punto flotante, False de lo contrario.
    """
    if validate_str(number):

        pattern = re.compile(r'^[+-]?\d+(\.\d+)+$')
        
        if pattern.match(number):
            return True
        else:
            return False
    else:
        return False
    
    