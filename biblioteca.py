
"""
def validar_int_str(key:str) -> int or list : 
    if re.search("^[0-9]+$", key):
       resultado = int(key)   

    elif re.search("^[a-z]+$", key, re.IGNORECASE):
        resultado = key
    else:
        return False        

    if(resultado != None and type(resultado) == int):
        return resultado
    elif(resultado != None and type(resultado) == str):
        return resultado
    else: 
        return False

def buscar_tipo(lista:list,key:str):
    
     for elemento in lista:
            for poke in elemento["tipo"]:
                poke_encontrado = re.search(key,poke,re.IGNORECASE)

                if(poke_encontrado != None):
                    print("ID:{0} | NOMBRE: {1} | TIPO: {2}".format(elemento["id"],elemento["nombre"],elemento["tipo"]))

def ordenar_lista (lista:list,key:str,order:str)->list:
    lista_a_ordenar = lista.copy() 
    lista_ordenada = []
    while(len(lista_a_ordenar)>0):
        index_min_max = buscar_min_max(lista_a_ordenar,key,order)
        elemento = lista_a_ordenar.pop(index_min_max)
        lista_ordenada.append(elemento)
    return lista_ordenada
"""