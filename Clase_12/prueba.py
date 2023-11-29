personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Buenos Aires"},
    {"nombre": "María", "edad": 30, "ciudad": "Córdoba"},
    {"nombre": "Pedro", "edad": 20, "ciudad": "Buenos Aires"},
    {"nombre": "Ana", "edad": 25, "ciudad": "Córdoba"}
]

def ordenar_lista(lista: list, key_1: str, key_2: str, key_3: str)->list:
    '''
    Ordena una lista por el método bubble sort, por 2 criterios, si por el primer criterio son iguales ahi recién
    ordena por el segundo criterio.
    Recibe la lista de diccionarios, y los 2 criterios por los cuales va ordenar la lista.
    Retorna la lista ordenada.
    '''
    if isinstance(lista, list) and lista:
        tamaño = len(lista)

        for i in range(0, tamaño - 1):
            for j in range(i + 1, tamaño):
                if lista[i][key_1] > lista[j][key_1]:
                    lista[i], lista[j] = lista[j], lista[i]

                elif lista[i][key_1] == lista[j][key_1]:
                    if lista[i][key_2] > lista[j][key_2]:
                        lista[i], lista[j] = lista[j], lista[i]
                        
                elif lista[i][key_2] == lista[j][key_2]:
                    if lista[i][key_3] > lista[j][key_3]:
                        lista[i], lista[j] = lista[j], lista[i]
        retorno = lista
    else:
        retorno = []
    
    return retorno


lista_ordenada = ordenar_lista(personas, "edad", "ciudad", "nombre")

for item in lista_ordenada:
    print("Nombre: {0} Edad: {1} Ciudad: {2}".format(item["nombre"],item["edad"], item["ciudad"]))