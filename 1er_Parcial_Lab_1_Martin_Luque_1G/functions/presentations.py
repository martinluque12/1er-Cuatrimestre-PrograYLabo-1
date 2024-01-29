from file_manager import *
from console_functions import *
from data_manipulation import *

    
def infobaus_read_file_supplies() -> list | None:
    """Lee el archivo CSV de los insumos.

    Returns:
        list | None: La lista de diccionarios  con la información de los insumos o
          imprime un mensaje de error si no se pudo leer el archivo.
    """
    file_path = "1er_Parcial_Lab_1_Martin_Luque_1G\\csv_file\\Insumos.csv - Hoja 1.csv"

    list_supplies = read_csv_supplies_file(file_path)

    if list_supplies:
        print("\nArchivo CSV cargado correctamente.")
        return list_supplies
    else:
        print("Error al cargar el archivo CSV.")


def infobaus_print_quantity_by_brand(data_list: list) -> None:
    """Función principal para filtrar y mostrar las marcas y sus cantidades.

    Args:
        data_list (list): La lista de diccionarios con la info de los insumos.
    """
    if validate_list(data_list):

        dictionary = list_quantity_by_key(data_list, "Marca")
        print_quantity_by_brand(dictionary)
    else:
        print("\nOrigen de datos no valido.")
