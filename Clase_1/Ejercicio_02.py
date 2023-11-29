"""
1G MARTIN LUQUE

Ejercicio 02

Debemos hacer un programa para que el usuario recuerde las reglas de estilo de python, entonces debemos pedirle al usuario
un número entre el 1 y el 8, al ingresar el número debemos mostrarle que regla de estilo representa 
y su descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario “Error, regla de estilo inexistente”
"""

while True:
    entered_number = input(
        "\n\nIngrese un numero del 1 al 8 según que regla de estilo de Python quiere conocer o 0 para salir. > "
    ).strip()

    match entered_number:
        case "1":
            mensaje = f"""
            *-----------------------------------------------------------------------------------------------*

            ¿Cual es es el sentido?
            Según Guido van Rossum, el código es leído más veces que escrito, por lo que resulta importante
            escribir código que no sólo funcione, sino que además pueda ser leído con facilidad.

            *-----------------------------------------------------------------------------------------------*
            """
            print(mensaje)

        case "2":
            mensaje = f"""
            *-----------------------------------------------------------------------------------------------*

            ¿Que es PEP?
            Python Enhancement Proposal es un documento que proporciona información a la comunidad de Python,
            o que describe una nueva característica.

            *-----------------------------------------------------------------------------------------------*
            """
            print(mensaje)

        case "3":
            mensaje = f"""
            *-----------------------------------------------------------------------------------------------*

            ¿Que es PEP 8?
            Es un conjunto de recomendaciones cuyo objetivo es ayudar a escribir código más legible y abarca
            desde cómo nombrar variables, al número máximo de caracteres que una línea debe tener.

            *-----------------------------------------------------------------------------------------------*
            """
            print(mensaje)

        case "4":
            mensaje = f"""
            *-----------------------------------------------------------------------------------------------*

            Identado.
            Python no usa {{}} para designar bloques de código como otros lenguajes de programación,
            sino que usa bloques identados para indicar que un determinado bloque de código pertenece
            a por ejemplo un if.

            *-----------------------------------------------------------------------------------------------*
            """
            print(mensaje)

        case "5":
            mensaje = f"""
            *-----------------------------------------------------------------------------------------------*

            Tamaño máximo de linea.
            Se recomienda limitar el tamaño de cada línea a 79 caracteres, para evitar tener que hacer scroll
            a la derecha.

            *-----------------------------------------------------------------------------------------------*
            """
            print(mensaje)

        case "6":
            mensaje = f"""
            *-----------------------------------------------------------------------------------------------*

            Lineas en blanco.
            El uso de espacios en blanco mejora la legibilidad del código, y es por lo que la PEP8 indica 
            dónde debemos usar espacios y dónde no.

            *-----------------------------------------------------------------------------------------------*
            """
            print(mensaje)

        case "7":
            mensaje = f"""
            *-----------------------------------------------------------------------------------------------*

            Comentarios.
            Cualquier comentario que contradiga el código es peor que ningún comentario. Si actualizamos el
            código, se debe actualizar los comentarios para evitar crear inconsistencias. Evitar comentarios
            poco descriptivos que no aporten nada más allá de lo que ya se ve a simple vista.

            *-----------------------------------------------------------------------------------------------*
            """
            print(mensaje)

        case "8":
            mensaje = f"""
            *-----------------------------------------------------------------------------------------------*

            Nombres:

            * Funciones: Uso de snake_case, letras en minúscula separadas por guion bajo: "mi_funcion".
            * Variables: Al igual que las funciones: variable, "mi_variable".
            * Clases: Uso de CamelCase, usando mayúscula y sin barra baja: "MiClase", "ClaseDePrueba".
            * Métodos: Al igual que las funciones, usar snake_case: método, "mi_metodo".
            * Constantes: Nombrarlas usando mayúsculas y separadas por guion bajas: "UNA_CONSTANTE".
            * Módulos: Igual que las funciones: "modulo.py", "mi_modulo.py".

            *-----------------------------------------------------------------------------------------------*
            """
            print(mensaje)

        case "0":
            break
        case _:
            print("\n¡Error! Regla de estilo inexistente.")
            continue