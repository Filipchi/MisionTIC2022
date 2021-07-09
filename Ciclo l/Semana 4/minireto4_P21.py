import os
os.system("cls")

print("------------------MiniReto 4 ------------------")

def leucocitos(info:dict)-> tuple: 
    # Se accede la información de las cedulas por medio del metodo .keys()
    cedulas = info.keys()
    resultado = {}
    for i in cedulas:
        dias = info[i]["infoHemograma"].keys()
        leuco = info[i]["infoHemograma"].values()
        #se crea el for interno con el objetivo de almacenar el 
        #promedio de leucocitos por paciente
        #Iniciamos variable acumuladora
        suma = 0
        cantidadDias = len(dias)
        for diasItems, leucoItems in (info[i]["infoHemograma"].items()):
            suma = suma + leucoItems
        resultado[i]= round(suma / cantidadDias, 1)
        
        leucoMayor10 = dict(filter(lambda leuco : leuco[1] >= 10.1 ,resultado.items()))
    
    return (resultado,leucoMayor10) 

info1 = {
    1144154: {
        "nombreCompleto": "Juan Perez",
        "infoHemograma":
            {
                "dia1":22.5,"dia2":25.6,"dia3":26.7,"dia4":19.5,"dia5":20.1
            }
    },
    1088852: {
        "nombreCompleto": "Mariana Pajón",
        "infoHemograma":
            {
                "dia1": 9.5, "dia2": 7.8, "dia3": 9.7, "dia4": 8.1, "dia5": 6.3
            }
    },
    1664558: {
        "nombreCompleto": "Leydi Torres",
        "infoHemograma":
            {
                "dia1":30.5,"dia2":27.6,"dia3":28.7,"dia4":21.5,"dia5":21.1
            }
    },
    1745558: {
        "nombreCompleto": "Leydi2 Torres",
        "infoHemograma":
            {
                "dia1":40.5,"dia2":25.6,"dia3":15.7,"dia4":17.5,"dia5":18.1
            }
    }
}

print(leucocitos(info1))
