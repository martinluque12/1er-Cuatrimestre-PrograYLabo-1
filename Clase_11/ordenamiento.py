# #burbujeo
# lista = [3,4,5,6,7,34,45,6,7,1]

# tam = len(lista)

# for i in range(0,tam-1):
#     for j in range(i+1,tam):
#         if lista[i] < lista[j]:
#             lista[i], lista[j] = lista[j], lista[i]


# print(lista)

# def ordenar_por_key(lista: list, key_1: str, key_2: str):
#     '''
#     '''
#     tam = len(lista)

#     for i in range(0, tam - 1):
#         for j in range(i+1, tam):
            
#             if lista[i][key_1] > lista[j][key_1]:
#                 lista[i], lista[j] = lista[j], lista[i]
#             elif lista[i][key_1] == lista[j][key_1] and float(lista[i][key_2].replace("$", "")) < float(lista[j][key_2].replace("$", "")):
#                 lista[i], lista[j] = lista[j], lista[i]

#     return lista

# def ordenar_lista(lista:list,group: str, key: str, asc=True):
#     tam = len(lista)

#     for i in range(0, tam - 1):
#         for j in range(i + 1, tam):
#             if(lista[i][group] == lista[j][group] and lista[i][key] > lista[j][key] or
#                lista[i][group] > lista[j][group]):
#                 lista[i], lista[j] = lista[j], lista[i]

        
    
# ordenar_lista(lista_personajes,"color_ojos","peso")

# for heroe in lista_personajes:
#     print(heroe)

# from functools import reduce
# #pares = list(filter(lambda heroe: heroe["editorial"] == "Marvel", lista_personajes))

# mujeres = reduce(lambda ant, act: ant + float(act["fuerza"]), list(filter(lambda h: h["genero"] == "F", lista_personajes)),0)

# print(mujeres)
