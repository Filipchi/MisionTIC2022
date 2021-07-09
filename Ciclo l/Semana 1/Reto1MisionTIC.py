import os
os.system ("cls")

print(f"\n\n\t ***************************************************")
print(f"\t * Bienvenidos Al Calculo de Su Factura Telefónica *")
print(f"\t ***************************************************\n\n")


def factura_celular(numeroSuscriptor, costoDelPlan, numeroMinutosPlan, cargoPorMinutoExtra, minutosConsumidos):
    Subtotal = costoDelPlan + ((minutosConsumidos - numeroMinutosPlan) * cargoPorMinutoExtra)
    Iva = Subtotal * 0.19
    TotalFactura = Subtotal + Iva

    return f"El cliente {numeroSuscriptor} debe cancelar: {TotalFactura} pesos"

print(factura_celular("DIC986", 30000, 100, 400, 150), f"\n")
print(factura_celular("AMG567", 40000, 150, 250, 300), f"\n")

