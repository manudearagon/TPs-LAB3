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
dataApi = r.json()# convertimos a json

# convertimos en dos data frame las colmnas de poblacion y pais
data = pd.DataFrame(dataApi['Countries'])# convertimos el json a un data frame

# asignamos los datos a las variables
pais = data.sort_values(by=['TotalDeaths'], ascending=False)

x = pais['TotalDeaths']
y = pais['Country']


#graficamos
plt.figure(figsize=(40, 20))
sns.barplot(y[:20], x[:20])
plt.xlabel('Pais', fontsize=50)
plt.ylabel('Muertes', fontsize=50)
plt.show()


