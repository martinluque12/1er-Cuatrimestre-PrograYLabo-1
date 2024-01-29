from validations import *

def castear_int(entero_str: str) -> int:
    """Castea una variable str que contiene solo caracteres numéricos a int.

    Args:
        entero_str (str): La variable a castear.

    Returns:
        int: La variable casteada a int si es que contiene solo caracteres numéricos,
            de lo contrario False.
    """
    if validate_int(entero_str):
        return int(entero_str)
    else:
        return 0
    

def castear_float(flotante_str: str) -> float | int:
    """Castea una variable str que contiene  un número con punto flotante.

    Args:
        flotante_str (str): La variable a castear.

    Returns:
        float | int: La variable casteada a float o 0 si no pasa la validación.
    """
    if validate_float(flotante_str):
        return float(flotante_str)
    else:
        return 0