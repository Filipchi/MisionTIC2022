import os
import numpy as np
os.system("cls")

def imc(info: dict) -> tuple:
    cedulas = info.keys()
    promedioIMC = {}
    IMC = []
    for x in cedulas:
        for j in range(len(info[x]["infoSalud"]["peso"])):
            peso = info[x]["infoSalud"]["peso"][j]
            altura = info[x]["infoSalud"]["altura"][j]
            IMC.append(peso / (altura**2))
        promedioIMC[x] = round(np.mean(IMC) , 1)
        IMCmayor25 = dict(filter(lambda mayor : mayor[1] >= 25 , promedioIMC.items()))
        IMC = []
    return (promedioIMC, IMCmayor25)

# Entradas
info1 = {
    1144154: {
        "nombreCompleto": "Lina Maria Valencia",
        "infoSalud":
        {
            "peso": [70, 75, 80, 85, 86],
            "altura": [1.8, 1.8, 1.8, 1.8, 1.8]
        }
    },
    1088852: {
        "nombreCompleto": "Mariana Sandoval",
        "infoSalud":
        {
            "peso": [55, 50, 60, 62, 70],
            "altura": [1.7, 1.7, 1.7, 1.7, 1.7]
        }
    },
    1664558: {
        "nombreCompleto": "Sara Torres",
        "infoSalud":
        {
            "peso": [50, 40, 45, 50, 60],
            "altura": [1.50, 1.51, 1.52, 1.55, 1.6]
        }
    }
}
info2 = {
    6668145: {
        "nombreCompleto": "Pablo Perez",
        "infoSalud":
        {
            "peso": [70, 75, 85, 85, 86],
            "altura": [1.6, 1.6, 1.6, 1.6, 1.6]
        }
    },
    7412589: {
        "nombreCompleto": "Juan Esteban Sanchez",
        "infoSalud":
        {
            "peso": [40, 50, 41, 42, 43],
            "altura": [1.45, 1.46, 1.47, 1.48, 1.5]
        }
    },
    9632145: {
        "nombreCompleto": "Daniel Molano",
        "infoSalud":
        {
            "peso": [60, 61, 62, 63, 64],
            "altura": [1.55, 1.55, 1.55, 1.55, 1.55]
        }
    }
}
print(imc(info1), "\n\n",imc(info2))
# ({1144154: 24.4, 1088852: 20.6, 1664558: 20.7}, {})
# ({6668145: 31.3, 7412589: 19.9, 9632145: 25.8}, {6668145: 31.3, 9632145: 25.8})
os.system("pause")
os.system("cls")