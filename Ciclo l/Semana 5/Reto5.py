import os
import pandas as pd
os.system("cls")

def calificaciones(ruta_archivo:str)-> dict:
    lectura = pd.read_csv(ruta_archivo)
    asignaturas = list(lectura.columns[5:lectura.shape[1]])
    promedios = [sum([lectura[x][y]/len(lectura) for y in range(len(lectura))]) for x in asignaturas]
    
    return {"promedioGeneral": round(sum(promedios) / 5, 1),
            "promedioNaturales": round(promedios[3], 1),
            "promedioMatematicas": round(promedios[1], 1)
            }
print(calificaciones("https://bitbucket.org/insuasti/datosreto5mintic/raw/c7a27c4a984ee1f427eedca949f8aed22f31f244/calificaciones.csv"))