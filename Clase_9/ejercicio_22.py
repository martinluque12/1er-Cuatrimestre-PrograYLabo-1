import re     

tema = {
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
}

# Tipo : BZRP MUSIC SESSIONS
# Artista: QUEVEDO
# Numero: 52
# Reproducciones: 227 M
# Duración: 204 segundos
# Codigo: A_g3lMcWVy0
# Fecha de carga:6/7/2022
# Hora de carga: 00:00

def split_string(pattern: str, dictionary: dict, key: str) -> list:
    """Divide una cadena de string, de una clave de un diccionario, en una lista 
       (desde el patron que se le pase por parámetro).

    Args:
        pattern (str): El patron desde el cual se va a dividir la cadena.
        dictionary (dict): El diccionario en el cual se quiere dividir la cadena.
        key (str): La clave del diccionario en la cual se va a buscar el patron.

    Returns:
        list: Una lista de la cadena dividida.
    """
    pattern_found = re.split(pattern, dictionary[key])

    return pattern_found

def format_views(dictionary: dict, key: str) -> float:
    """Formatea las vistas del video.

    Args:
        dictionary (dict): El diccionario donde esta la info del video.
        key (str): La clave donde se encuentra la información de las vistas.

    Returns:
        str: Las vistas formateadas un formato "100.000".
    """
    duration = dictionary[key] / 1000000

    return duration

def find_code(pattern: str, dictionary: dict, key: str) -> list:
    """Busca el código del video 

    Args:
        pattern (str): El patron a buscar par encontrar el código.
        dictionary (dict): El diccionario donde esta la info del video.
        key (str): La clave donde se encuentra la información del código.

    Returns:
        list: Una lista con el código en str.
    """
    code_found = re.findall(pattern, dictionary[key], re.IGNORECASE)

    return code_found

def format_date(dictionary: dict) -> str:
    """Formatea la fecha de carga del video.

    Args:
        dictionary (dict): El diccionario donde esta la info del video.

    Returns:
        str: La fecha de carga formateada.
    """
    date = re.split(" ", dictionary["date"])
    date = date[0]
    date = re.split("-", date)
    date[0], date[2] = date[2], date[0]
    date = "/".join(date)

    return date
    
def format_time(dictionary: dict) -> str:
    """Formatea la hora de carga.

    Args:
        dictionary (dict): El diccionario donde esta la info del video.

    Returns:
        str: La hora de carga formateada.
    """
    time = re.split(" ", dictionary["date"])

    time_format = time[1]

    return time_format[:5]

def show_on_console() -> None:
    """Muestra por consola la descripción del video formateada de una manera especifica.
    """
    title = split_string(" #| \|{2} ", tema, "title")
    reproductions = format_views(tema, "views")
    duration = tema["length"]
    code = find_code("A_.+", tema, "url")
    date = format_date(tema)
    time = format_time(tema)

    print("*"*50)                
    print("Titulo: {0} \nArtista: {1} \nNumero: {2}".format(title[1], title[0], title[2]))
    print("Reproducciones: {0:.2f}M \nDuración: {1} seg".format(reproductions, duration))
    print("Código: {0} \nFecha de carga: {1} \nHora de carga: {2}".format(code[0], date, time))
    print("*"*50)  

show_on_console()