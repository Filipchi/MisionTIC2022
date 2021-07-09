import os
os.system("cls")

def prestamo(informacion: dict) -> dict:
    id_prestamo = informacion["id_prestamo"]
    # hCredito = informacion["historia_credito"]
    # i_c = informacion["ingreso_codeudor"]
    # i_d = informacion["ingreso_deudor"]
    # c_p = informacion["cantidad_prestamo"]
    # dep = informacion["dependientes"]
    # indep = informacion["independiente"]
    
    aprobado = False

    if informacion["casado"] == "Si" or informacion["casado"] == "si":
        informacion["casado"] = True
    else:
        informacion["casado"] = False

    if informacion["independiente"] == "Si" or informacion["independiente"] == "si":
        informacion["independiente"] = True
    else:
        informacion["independiente"] = False
    
    if informacion["dependientes"] == "3+" :
        informacion["dependientes"] = 3

    if (informacion["historia_credito"] == 1):
        if ((informacion["ingreso_codeudor"] > 0) and (informacion["ingreso_deudor"] / 9 > informacion["cantidad_prestamo"])):    
            aprobado = True  # 1        

        else:
            if ((informacion["dependientes"] > 2) and informacion["independiente"]):
                if informacion["ingreso_codeudor"] / 12 > informacion["cantidad_prestamo"]: # 2
                    aprobado = True  # 2

            elif informacion["cantidad_prestamo"] < 200:
                aprobado = True  # 3
    else:
        if (informacion["independiente"] == True):
            if (not(informacion["casado"]) and informacion["dependientes"] > 1):
                if (((informacion["ingreso_deudor"]/10) > informacion["cantidad_prestamo"]) and 
                    ((informacion["ingreso_codeudor"]/10) > informacion["cantidad_prestamo"])):
                    
                    if informacion["cantidad_prestamo"] < 180:
                        aprobado = True   # 4
                else:
                    aprobado = False  # 5
            else:
                aprobado = False  # 6
        else:
            if (not(informacion["tipo_propiedad"] == "Semiurbano") and 
                (informacion["dependientes"] < 2)):

                if (informacion["educacion"] == "Graduado"):
                    if ((informacion["ingreso_deudor"] / 11 > informacion["cantidad_prestamo"]) and (informacion["ingreso_codeudor"] / 11 > informacion["cantidad_prestamo"])):

                        aprobado = True  # 7
                else:
                    aprobado = False  # 9
            else:
                aprobado = False  # 10

    diccionario_salida = {
        "id_prestamo": id_prestamo,
        "aprobado": aprobado
    }

    return diccionario_salida


# informacion = {
#     "id_prestamo": "RETOS2_001",
#     "casado" : "No",
#     "dependientes" : 1,
#     "educacion" : "Graduado",
#     "independiente" : "Si",
#     "ingreso_deudor" : 4692,
#     "ingreso_codeudor" : 0,
#     "cantidad_prestamo" : 106,
#     "plazo_prestamo" : 360,
#     "historia_credito" : 1,
#     "tipo_propiedad" : "Rural",
# }

# informacion = {
#     "id_prestamo": "RETOS2_002",
#     "casado": "No",
#     "dependientes": "3+",
#     "educacion": "No Graduado",
#     "independiente": "No",
#     "ingreso_deudor": 1830,
#     "ingreso_codeudor": 0,
#     "cantidad_prestamo": 100,
#     "plazo_prestamo": 360,
#     "historia_credito": 0,
#     "tipo_propiedad": "Urbano",
# }

informacion = {
     "id_prestamo": "RETOS2_003",
     "casado": "No",
     "dependientes": 0,
     "educacion": "Graduado",
     "independiente": "Si",
     "ingreso_deudor": 1668,
     "ingreso_codeudor": 0,
     "cantidad_prestamo": 110,
     "plazo_prestamo": 360,
     "historia_credito": 1,
     "tipo_propiedad": "Semiurbano",
}

print (f"\n\t", prestamo(informacion), f"\n")
