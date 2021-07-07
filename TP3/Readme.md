#  <center>Trabajo Practico 3
##  Beautiful Soup 
### Por: Lucas Manuel Moyano - Juan Manuel de Aragón
### Universidad Blas Pascal
---
![Beautiful Soup](https://i.postimg.cc/653tWBy9/68747470733a2f2f64333377756272666b69306c36382e636c6f756466726f6e742e6e65742f646131653033313836323264.png)

## Información clave para poder comprender Beautiful Soup

 - [Python](https://es.wikipedia.org/wiki/Python "Python") 
 - [Web Scrapping](https://es.wikipedia.org/wiki/Web_scraping "Web Scrapping") 
 -  [HTML](https://es.wikipedia.org/wiki/HTML"HTML")

# <center> ¿Qué es Beautiful Soup?

>Beautiful Soup es una biblioteca de Python para extraer datos de archivos HTML y XML. Proporciona formas características de navegar, buscar y modificar el árbol de análisis. Por lo general, ahorra a los programadores mucho tiempo de trabajo, ya que las búsquedas son mucho más simples de realizar.
---

#  <p align=center>  Trabajando con Beautiful Soup 

### Guía Básica 
![enter image description here](https://tedboy.github.io/bs4_doc/_images/6.1.jpg)

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
## <p align=center>    ![enter image description here](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDe_ChmuOQPKCeam6XPP52quOlvv0HIfNk7Q&usqp=CAU)
