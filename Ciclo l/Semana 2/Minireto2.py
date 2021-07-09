import os
os.system("cls")

def factura_supermercado(informacion:dict)->dict:
    numero_cliente = informacion["id_cliente"]
    precio_procucto1 = informacion["producto 1"]
    precio_procucto2 = informacion["producto 2"]
    precio_procucto3 = informacion["producto 3"]
    precio_procucto4 = informacion["producto 4"]
    precio_procucto5 = informacion["producto 5"]
    precio_carne_res = informacion["carne de res"]

    subtotal = precio_procucto1 + precio_procucto2 + \
        precio_procucto3 + precio_procucto4 + precio_procucto5 + precio_carne_res

    iva = 0
    valor_adicional = 0

    if subtotal > 150000 and subtotal <= 300000:
        iva = subtotal * 0.1
        if precio_carne_res > 0:
            valor_adicional = subtotal * 0.01
        else:
            valor_adicional = 0
    elif subtotal <= 300000:
        iva = subtotal * 0.15
        if precio_carne_res > 0:
            valor_adicional = subtotal * 0.01
        else:
            valor_adicional = 0
    
    valor_total = subtotal + iva + valor_adicional
    valor_total = round(valor_total,1)

    diccionario_respuesta = {
        "id_cliente" : numero_cliente,
        "subtotal" : subtotal,
        "iva" : iva,
        "adicionalcarne" : valor_adicional,
        "Total" : valor_total
    }

    return diccionario_respuesta


datos_entrada = {
    "id_cliente" : 67,
    "producto 1" : 3200, 
    "producto 2" : 6500,
    "producto 3" : 98000,
    "producto 4" : 65000,
    "producto 5" : 55000,
    "carne de res" : 5000
}

print(factura_supermercado(datos_entrada)) 
    

