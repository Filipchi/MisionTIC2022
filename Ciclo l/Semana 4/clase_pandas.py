import os
from numpy import DataSource
os.system("cls")

import pandas as pd

# Dataframe: conjunto de series que forman una tabla con la librería pandas
datos = {"manzanas" : [1, 2, 3, 4, 5], "naranjas" : [6, 7, 8, 9, 10]}
compras = pd.DataFrame(datos, index = ["Deyci", "Jess", "Nata", "Valen", "Lu"])
print(compras)

# Para cambiarle el nombre a las columnas del dataframe
compras.index.name = "Clientes"
compras.columns.name = "Productos"
print(compras)