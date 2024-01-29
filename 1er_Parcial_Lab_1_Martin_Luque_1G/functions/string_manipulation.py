from validations import *


def capitalize_word(string: str) -> str:
    """Pone en mayúscula cada primer letra de una cadena de texto.

    Args:
        string (str): La cadena de texto a capitalizar.

    Returns:
        str: Retorna la cadena pero con cada primer letra en mayúscula.
    """
    if validate_str(string):

        string = string.strip()
        string = string.split(" ")
        string_capitalizado = []

        for word in string:
            word = word.capitalize()
            string_capitalizado.append(word)

        string_capitalizado = " ".join(word + "" for word in string_capitalizado)

        return string_capitalizado
    
    else:
        return ""