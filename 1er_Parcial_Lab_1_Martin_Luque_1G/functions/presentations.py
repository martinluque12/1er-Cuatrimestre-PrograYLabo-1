from file_manager import *

def infobaus_read_csv_file_supplies() -> list:
    """Lee el archivo CSV con la info de los insumos mediante la función "read_csv_file_supplies()"
       y lo convierte en una lista de diccionarios.

    Returns:
        list: La lista de diccionarios con la información de los insumos.
    """
    file_path = "1er_Parcial_Lab_1_Martin_Luque_1G\\csv_file\\Insumos.csv - Hoja 1.csv"
    list_supplies = read_csv_file_supplies(file_path)

    if file_path:
        print("Se ha leido el archivo correctamente.")
        return list_supplies
    else:
        print("Error al leer el archivo.")
        return []
    
