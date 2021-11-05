#  <center>Trabajo Practico 6
#  Django

### Por: Lucas Manuel Moyano - Juan Manuel de Aragón
### Universidad Blas Pascal
![enter image description here](https://swapps.com/wp-content/uploads/2019/04/django-faster.jpg)
---
## Tutorial para la creación de un entorno virtual

 - **Instalar el VirtualEnv:**
	 - pip install virtualenvwrapper-win
 - **Crear un entorno virtual**
	-	mkvirtualenv NOMBRE DEL ENTORNO
 - **Ingresar al entorno virtual**
	- workon NOMBRE DEL ENTORNO
 - **Salir del entorno virtual**
	- deactivate
 - **Eliminar un entorno virtual**
	- rmvirtualenv NOMBRE DEL ENTORNO
 - **Ver lista de entornos virtuales creados**
	- workon
--- 
## Hacer un proyecto en Django
 - [ ] Hacer el entorno virtual con el virtualenvwrapper
 - [ ] pip install django
 - [ ] django-admin startproject	NOMBRE DEL PROYECTO
	 - [ ] Con el manage.py podemos ejecutar los comandos de Django
 - [ ] Dentro de la carpeta que posee el nombre del proyecto corroborar que esten correctos estos archivos
	 - asgy.py y wsgi.py (archivos de configuración para los servidores que escuchan las peticiones)
	 - settings.py (todas las configuraciones principales del proyecto)
	 - urls.py (rutas que definen para que el correspondiente URL ejecute la función correspondiente)
 - [ ] python manage.py runserver (Arranca el servidor y nos brinda la url del mismo)
 - [ ] Abrir el proyecto en VsCode y renombrar
 - La capeta llamada "nombredelproyecto" se la renombra por "config"
 - En el archvio asgi.py y wsgi.py:
	 - En la linea 14, donde dice: "nombredelproyecto" cambairlo por "config"
 - En el archvio settings.py:
	- Cambiar todos los "nombredelproyecto" por "config"
 - En el archivo manage.py:
	- Cambiar el "nombredelproyecto" por "config"
 - [ ] python manage.py startapp "nombredelaapp"

--- 
## Informacion adicional de Django

 - https://www.youtube.com/watch?v=7XO1AzwkPPE
 - https://www.djangoproject.com/

---
## Descripción del proyecto

## Información clave para comprender el trabajo practico

 

