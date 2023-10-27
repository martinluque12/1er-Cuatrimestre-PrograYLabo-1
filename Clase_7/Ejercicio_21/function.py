import os

def clear_console() -> None:
    """
    Limpia la consola.
    """
    os.system('cls')

def load_temp_and_days() -> list:
    """
    Pide que se ingrese un dia y una temperatura de cada dia de la semana.

    Returns:
        dict: Retorna una lista de diccionarios con el dia y su temperatura.
    """
    DAYS_WEEK = 7
    list_days_temperature = []
    
    while len(list_days_temperature) < DAYS_WEEK:
        entered_day = request_day()
        
        day_exist = False
        for item in list_days_temperature:
            if item["day"] == entered_day:
                day_exist = True
                break

        if not day_exist:
            entered_temperature = request_temp()
            day_temperature = {"day": entered_day, "temperature": entered_temperature}

            list_days_temperature.append(day_temperature)
        else:
            print("\nEl día ya fue cargado, ingrese uno distinto.")

    return list_days_temperature

def request_day() -> str:
    """
    Pide que se ingrese un dia de la semana y lo valida.
    Returns:
        str: Retorna el dia que se ingreso.
    """
    day = input("\nIngrese un dia de la semana > ").strip()

    while(day.lower() != "lunes" and day.lower() != "martes" and day.lower() != "miercoles" and
          day.lower() != "jueves" and day.lower() != "viernes" and day.lower() != "sabado" and
          day.lower() != "domingo"):
        
        day = input("\n¡Error! Dia no valido, vuelva a intentarlo > ").strip()

    return day.capitalize()
    

def request_temp() -> float:
    """
    Pide que ingresen una temperatura y valida que se ingrese un carácter numérico mayor a 0 
    y en un rango especifico.
    Returns:
        float: Retorna la temperatura.
    """
    while True:
        try:
            temperature = float(input("\nIngrese la temperatura en grados Celsius > ").strip())
            while temperature < -89 or temperature > 54:
                temperature = float(input("\n¡Error! Debe ingresar un carácter numérico entre -89° y 54°,"
                                          " vuelva a intentarlo > ").strip())
                
            return temperature
        
        except ValueError:
            print("¡Error! Solo se permiten caracteres numéricos.")
    
def calculate_temp_average(list: list) -> float:
    """
    Calcula el promedio de las temperaturas ingresadas en una lista de diccionarios.
    Args:
        list (list): La lista de diccionarios que contiene las temperaturas.

    Returns:
        float: Retorna el promedio de temperaturas.
    """
    totals_temperatures = 0

    for temperature in list:
        totals_temperatures += temperature["temperature"]

    average = totals_temperatures / len(list)

    return average

def calculate_max_temp(list: list) -> list:
    """
    Calcula la temperatura maxima ingresada en una lista de diccionarios.
    Args:
        list (list): La lista de diccionarios que contiene las temperaturas.

    Returns:
        list: Retorna una lista de diccionarios que contiene la o las temperaturas máximas.
    """
    max_temperature = list[0]
    list_max_temperature = []

    for item in list:
        if item["temperature"] > max_temperature["temperature"]:
            max_temperature = item
            list_max_temperature = [max_temperature]
        elif item["temperature"] == max_temperature["temperature"]:
            list_max_temperature.append(item)

    return list_max_temperature

def menu():

    load = False
    options_message = """
    1 - Cargar días y temperaturas.
    2 - Mostrar los días y sus temperaturas.
    3 - Mostrar la temperatura maxima y su dia.
    4 - Salir. \n\n    > """

    while True:

        clear_console()

        options = input(options_message)

        match options:

            case "1":
                if not load:
                    load = True
                    list = load_temp_and_days()
                else:
                    print("\nYa se han cargado los días y las temperaturas.")
            case "2":
                if load:
                    for item in list:
                        print("\nDia: {0:<12} | Temperatura: °{1}".format(item["day"], item["temperature"]))
                else:
                    print("\nPrimero debe cargas los días y sus temperaturas.")
            case "3":
                if load:
                    list_temp_max = calculate_max_temp(list)

                    for item in list_temp_max:
                        print("\nDia: {0:<12} | Temperatura Maxima: °{1}".format(item["day"], item["temperature"]))
                else:
                    print("\nPrimero debe cargas los días y sus temperaturas.")
            case "4":
                confirm_exit = input("\n¿Seguro que quiere salir? Responda con si o con no > ").lower()
                if confirm_exit == "si":
                    break
            case _:
                print("\nOpción no valida")
                continue
    
        input("\nPresione Enter para continuar...")
