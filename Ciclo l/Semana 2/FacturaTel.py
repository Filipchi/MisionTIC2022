import os
os.system("cls")

def factura_celular(informacion: dict)-> dict:
    nSuscriptor = informacion["numeroSuscriptor"]
    costoPlan = informacion["costoDelPlan"]
    minPlan = informacion["numeroMinutosPlan"]
    minExtra = informacion["cargoPorMinutoExtra"]
    minConsumidos = informacion["minutosConsumidos"]
    Estrato = informacion["estrato"]

    if minConsumidos > minPlan:
        Subtotal = costoPlan + ((minConsumidos - minPlan) * minExtra)
    else:
        Subtotal = costoPlan

    Iva = 0
    valorSeguro = 0

    if Subtotal >= 72000:
        Iva = Subtotal * 0.19
        if Estrato <= 3:
            valorSeguro = 5000
        else:
            valorSeguro = 6000
    else:
        if Estrato <= 3:
            valorSeguro = 4000
        else:
            valorSeguro = 4500

    totalFactura = Subtotal + Iva + valorSeguro
    
    diccionario_salida = {
        "numeroSuscriptor": nSuscriptor,
        "valorImpuesto": Iva,
        "valorSeguro": valorSeguro,
        "totalFactura": totalFactura
    }

    return diccionario_salida

datos_entrada = {
    "numeroSuscriptor": "ABC123",
    "costoDelPlan" : 73000,
    "numeroMinutosPlan" : 500,
    "cargoPorMinutoExtra": 300,
    "minutosConsumidos": 100,
    "Estrato" : 1
}

print(factura_celular(datos_entrada))
