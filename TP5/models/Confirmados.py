import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import requests

sns.set_theme(style="white", context="talk")

# ▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒
# ▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒
# ▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒
# ▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒
# ▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒

# consulta GET
r = requests.get('https://api.covid19api.com/summary')

# api covid
dataApi = r.json()  # convertimos a json
data = pd.DataFrame(dataApi['Countries'])  # convertimos el json a un data frame

# ordenamos el dataframe segun la consigna
pais = data.sort_values(by=['TotalConfirmed'], ascending=False)

pais_cp = (pais[:20])  # obtenemos solo los primeros 20

# asignamos datos a las variables
y = pais_cp['TotalConfirmed']
x = pais_cp['Country']

# graficamos la data obtenida
plt.figure(figsize=(40, 20))
sns.barplot(x, y, palette="rocket")
plt.xlabel('Paises', fontsize=50)
plt.ylabel('Porcentaje de Contagios', fontsize=50)
plt.show()
