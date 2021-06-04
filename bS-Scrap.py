import requests
from bs4 import BeautifulSoup
import csv

#Hacemos una petición con request para poder extraer el html y la guarda en page
page = requests.get('https://parascrapear.com/')

#Creamos una variable soup para usar el analizador (parser) 
soup = BeautifulSoup(page.text, 'html.parser')

# f = csv.writer(open('scrap.csv', 'w'))
# f.writerow(['Autor','Categoria','Frase'])


#Vamos a crear un array para hacer la extraccion de determinadas etiquetas html y poder recorrer
# ese arrays.(En este caso vamos a utilizar los blockquote)
blockquote_items = soup.find_all('blockquote')
for blockquote in blockquote_items:
    #en este caso vamos a extraer la info de diferentes clases que estan dentro de este vector
    
    #extraemos el autor que esta dentro de esta clase en el html
    autor = blockquote.find(class_= 'author').text
    
    #utilizamos las funciones de soup ej: find, soup, text; para poder extraer informacion de
    #determinadas clases dentro del html

    #extraemos la categoria que esta dentro de esta clase en el html
    categoria = blockquote.find(class_= 'cat').text

    #y extraemos una frase
    frase = blockquote.find('q').text

    # f.writerows([autor, categoria, frase])

    print(f'EL autor: {autor}')
    print('-----------------')
    print(f'La categoria: {categoria}')
    print(f'Frase: {frase}')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------')

