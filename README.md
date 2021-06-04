#  <center>Trabajo Practico 3
##  Beautiful Soup 
### Por: Lucas Manuel Moyano - Juan Manuel de Aragón
### Universidad Blas Pascal
---

![enter image description here](https://d33wubrfki0l68.cloudfront.net/da1e0318622d0d2134f72714d248a339780799af/1be46/blog/python-web-scraping-beautiful-soup/beautiful_soup.png)


## Información clave para poder comprender Beautiful Soup

 - [Python](https://es.wikipedia.org/wiki/Python "Python") 
 - [Web Scrapping](https://es.wikipedia.org/wiki/Web_scraping "Web Scrapping") 
 -  [HTML](https://es.wikipedia.org/wiki/HTML"HTML")

# <center> ¿Qué es Beautiful Soup?

>Beautiful Soup es una biblioteca de Python para extraer datos de archivos HTML y XML. Proporciona formas características de navegar, buscar y modificar el árbol de análisis. Por lo general, ahorra a los programadores mucho tiempo de trabajo, ya que las búsquedas son mucho más simples de realizar.
---
### Guía Básica 

#### Ejemplo de HTML  

        html_doc = """<html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    
    <p class="story">...</p>


#### Al cargar el archivo en BS, nos brinda un tipo de documento editado para poder ser trabajado con la librería

        from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print(soup.prettify())
    # <html>
    #  <head>
    #   <title>
    #    The Dormouse's story
    #   </title>
    #  </head>
    #  <body>
    #   <p class="title">
    #    <b>
    #     The Dormouse's story
    #    </b>
    #   </p>
    #   <p class="story">
    #    Once upon a time there were three little sisters; and their names were
    #    <a class="sister" href="http://example.com/elsie" id="link1">
    #     Elsie
    #    </a>
    #    ,
    #    <a class="sister" href="http://example.com/lacie" id="link2">
    #     Lacie
    #    </a>
    #    and
    #    <a class="sister" href="http://example.com/tillie" id="link3">
    #     Tillie
    #    </a>
    #    ; and they lived at the bottom of a well.
    #   </p>
    #   <p class="story">
    #    ...
    #   </p>
    #  </body>
    # </html>
#### Algunos comandos útiles son

    soup.title
    # <title>The Dormouse's story</title>
    
    soup.title.name
    # u'title'
    
    soup.title.string
    # u'The Dormouse's story'
    
    soup.title.parent.name
    # u'head'
    
    soup.p
    # <p class="title"><b>The Dormouse's story</b></p>
    
    soup.p['class']
    # u'title'
    
    soup.a
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    
    soup.find_all('a')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
    
    soup.find(id="link3")
#### Una de las funcionalidades más comunes es la de buscar información que se encuentra en cierto lugar 

    for link in soup.find_all('a'): //Buscar dentro del parámetro <a>
        print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie
