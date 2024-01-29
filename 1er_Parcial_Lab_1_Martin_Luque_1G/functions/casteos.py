import re
from validations import *


def castear_int(number: str) -> int:
    """Castea una variable str que representa un numero entero a int.

    Args:
        number (str): La variable str que representa un numero entero.

    Returns:
        int: La variable casteada a int o 0 en caso de error.
    """
    if validate_int(number):
        return int(number)
    else:
        return 0


def castear_float(number: str) -> float | int:
    """Castea una variable str que representa un numero de punto flotante a float.

    Args:
        number (str): La variable str a castear.

    Returns:
        float | int: La variable casteada o 0 en caso de error.
    """
    if validate_float(number):
        return float(number)
    else:
        return 0
    
    