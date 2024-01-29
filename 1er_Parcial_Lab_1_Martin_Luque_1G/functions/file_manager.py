from validations import *
from casteos import *
from string_manipulation import *


def read_csv_supplies_file(file_path: str) -> list:
    """Lee el archivo CSV de los insumos y convierte su contenido en una lista de diccionarios.

    Args:
        file_path (str): La ruta del archivo CSV.

    Returns:
        list: El contenido del archivo CSV convertido a una lista de diccionarios.
    """
    if validate_str(file_path):

        items = []

        with open(file_path, 'r', encoding='utf-8') as csv_file:

            lines = csv_file.readlines()
            header = lines[0].split(',')
            header = [line.replace('"', '').strip().capitalize() for line in header] 

            for line in lines[1:]:
                line = line.split(',')
                line = [item.replace('"', '').replace('$', '').strip() for item in line]
                line = [item.replace('|!*|', ', ') for item in line]


                dictionary = {
                    header[0]: castear_int(line[0]),
                    header[1]: capitalize_word(line[1]),
                    header[2]: capitalize_word(line[2]),
                    header[3]: castear_float(line[3]),
                    header[4]: line[4]
                }
            
                items.append(dictionary)

        return items
    
    else:
        return []
    


