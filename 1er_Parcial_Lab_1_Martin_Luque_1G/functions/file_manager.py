from validations import *
from casteos import *
from string_manipulation import *


def read_csv_file_supplies(file_path: str) -> list:
    """Lee el archivo CSV que contiene la información de los insumos y lo convierte
       en una lista de diccionarios.

    Args:
        file_path (str): La ruta del archivo CSV.

    Returns:
        list: La lista de diccionarios con la información de los insumos.
    """
    if validate_str(file_path):

        supplies = []

        with open (file_path, 'r', encoding='utf-8') as csv_file:

            lines = csv_file.readlines()
            header = lines[0].split(',')
            header = [key.replace('"', '').strip().lower() for key in header]

            for line in lines[1:]:
                line = line.split(',')
                line = [value.replace('"', '').replace('$', '').strip() for value in line]
                line = [value.replace('|!*|', ', ') for value in line]

                products = {
                    header[0]: castear_int(line[0]),
                    header[1]: capitalize_word(line[1]),
                    header[2]: capitalize_word(line[2]),
                    header[3]: castear_float(line[3]),
                    header[4]: line[4]
                }

                supplies.append(products)
        
        return supplies

    else:
        return []
    