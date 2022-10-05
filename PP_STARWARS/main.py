'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

def starwars_app():
    url_archivo = r"C:\Users\pablo\Desktop\Parcial\PP_STARWARS\data.json"
    lista_personajes = funciones.cargar_json(url_archivo)
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            funciones.mostar(funciones.ordenar_lista(lista_personajes,'height'))
            opcion1 = funciones.ordenar_lista(lista_personajes,'height')
        elif(respuesta=="2"):
            funciones.buscar_mas_alto(lista_personajes)
            opcion2 = funciones.buscar_mas_alto(lista_personajes)
        elif(respuesta=="3"): 
            funciones.ordenar_lista(lista_personajes,'mass',"mayor")
            opcion3 = funciones.ordenar_lista(lista_personajes,'mass',"mayor")
        elif(respuesta=="4"):
            print("4 - Armar un buscador de personajes\n")
            opcion4 =  print("4 - Armar un buscador de personajes\n")
        elif(respuesta=="5"):
            resp = input("¿Ingre una de las opcioens 1,2,3 o 4?")           
            if (resp == "1"):
                 funciones.exportar_csv(opcion1,r"C:\Users\pablo\Desktop\Parcial\PP_STARWARS\opcion1.csv")
            if (resp == "2"):
                 funciones.exportar_csv(opcion2,r"C:\Users\pablo\Desktop\Parcial\PP_STARWARS\opcion2.csv")
            if (resp == "3"):
                funciones.exportar_csv(opcion3,r"C:\Users\pablo\Desktop\Parcial\PP_STARWARS\opcion3.csv")
            if (resp == "4"):
                funciones.exportar_csv(opcion4,r"C:\Users\pablo\Desktop\Parcial\PP_STARWARS\opcion4.csv")
        elif(respuesta=="6"):
            break


starwars_app()

