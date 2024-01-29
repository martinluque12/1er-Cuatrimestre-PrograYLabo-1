from validations import *


def list_quantity_by_key(data_list: list, key: str) -> dict:
    """Filtra una lista de diccionarios por una clave y devuelve un diccionario con las ocurrencias 
       de cada valor en esa clave.

    Args:
        data_list (list): La lista de diccionarios.
        key (str): La clave por la que se va a filtrar.

    Returns:
        dict: Un diccionario con clave (El valor de la clave por la que se filtro) y valor 
             (La cantidad de ocurrencias del valor de la clave por la que se filtro.)
    """
    if validate_list(data_list) and validate_str(key):

        data_key = {}

        for item in data_list:    
            data_key[item[key]] = 0

        for item in data_list:
            data_key[item[key]] += 1

        return data_key
    else:
        return {}