import json


"""
{'name': 'Luke Skywalker',
 'height': '172',
  'mass': '77', 
  'gender': 'male'}


"""

def cargar_json(paht:str) -> list:

    with open(paht,"r") as file:
        buffer_dict = json.load(file)
    return buffer_dict["results"]


def ordenar_lista (lista:list,key:str,order:str="mayor") -> list:
    lista_a_ordenar = lista.copy() 
    lista_ordenada = []
    while(len(lista_a_ordenar)>0):
        index_min_max = buscar_min_max(lista_a_ordenar,key,order)
        elemento = lista_a_ordenar.pop(index_min_max)
        lista_ordenada.append(elemento)
    return lista_ordenada


def buscar_min_max(lista:list,key:str,order:str) -> list:
    retorno = -1
    if(len(lista) > 0):
        i_min_max = 0
        for i in range(len(lista)):
            if(order == "mayor" and lista[i][key] < lista[i_min_max][key])or (order == "menor" and lista[i][key] > lista[i_min_max][key]):
                i_min_max = i
        retorno = i_min_max
    return retorno

def mostar(lista:list) -> list:
    print("\n")
    for elemento in lista:
        print("1) {0} - 2) {1} - 3) {2} -4) {3} - ".format(elemento['name'],elemento['height'],elemento['mass'],elemento['gender'],))
    print("\n")


def buscar_mas_alto(lista:list) ->list:
    
    altura = lista[1]
    print(altura)
    for elemento in lista:
        print(elemento['height'])
        if (altura['height'] >= elemento['height'] ):
            altura = elemento['height']
            
        #elif(elemento['height'] > altura  and elemento['gender'] == key ):
          #  altura_f = elemento
        #else:
         #   altura_na = elemento
    
    return altura


def exportar_csv(lista:list,paht:str ) ->list:
    with open(paht,"w") as file:
        for elemento in lista:
            file.write("1) {0} - 2) {1} - 3) {2} -4) {3} - ".format(elemento['name'],elemento['height'],elemento['mass'],elemento['gender'],))
    print("\n")















