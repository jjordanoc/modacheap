# proyectodbp
Proyecto para el curso Desarrollo Basado en Plataformas.

## Nombre del proyecto

ModaCheap

## Integrantes
- Joaquín Francisco Jordán O`Connor 
- Enzo Gabriel Camizan Vidal
- Héctor Valentín Quezada Amour
- José Rafael Chachi Rodriguez

## Descripción del proyecto
Plataforma web en donde se realiza compra y venta de vestimenta de segunda mano para todo género.

## Objetivos principales / Misión / Visión
**Objetivos principales:** 

+ Realizar una exposición web de productos de ropa de segunda mano.
+ Permitir una comunicación entre el vendedor y comprador utilizando el API de WhatsApp.

**Misión:** Lo bueno, bonito y barato al alcance de un click.

**Visión:**  Ser el principal portal web de compra-venta de ropa de segunda mano en Lima.

## Información  acerca de las librerías/frameworks/plugins utilizadas en Front-end, Back-end y Base de datos.

**Front-end:**

Para agilizar el desarrollo front-end se utilizo Bootstrap 5.

Se utilizo Vue.js y Vue Client para nuestra interfaz de usuario y mejor experiencia

**Back-end:**

Para el desarrollo backend se emplearon las siguientes librerias/frameworks:
+ Flask
+ Flask SQLAlchemy
+ Flask Migrate
+ Werkzeug
+ Shortuuid
+ dotenv

**Base de datos:**

Para el desarrollo de la base de datos se utilizo unicamente PostgreSQL en su version 12.9.

## El nombre del script a ejecutar para iniciar la base de datos con datos.

Se debe crear un archivo `.env` en el directorio raiz del proyecto que establezca el valor de la variable `DATABASE_URI` al *URI* de nuestra base de datos local.

## Información acerca de los API. Requests y Responses de cada endpoint utilizado en el sistema.

+ `/` : Es la pagina principal de la aplicacion. Retorna el template index.html, sin el usuario ademas con todos los productos disponibles en la aplicacion
+ `/register` : Cuando el servidor recibe una solicitud POST, registra a el usuario con sus atributos, almacena la sesion del usuario y retorna un estado exitoso. Cuando ocurre algun error en el registro, retorna un estado fallido y un mensaje

+ `/login` : 
  * GET
    + Se inicia la sesion del usuario en la aplicacion y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.

+ `/products/` :
  + POST : 
    - El usuario puede crear los productos en la aplicacion web, mediante el metodo `POST`, y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.
+ `/products/<product_id>` :
  + PATCH : El usuario ya registrado y logeado en la pagina, podra modificar un producto que el haya creado, mediante el metodo `PATCH` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.
  
  + DELETE : El usuario ya registrado y logeado en la pagina, podra eliminar un producto que el haya creado, mediante el metodo `DELETE` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.

+ `/users` :
  - PATCH
    + EL usuario puede modificar sus atributos en la aplicacion mediante el metodo `PATCH` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.

  - DELETE  
    + El usuario puede eliminar su cuenta de la aplicacion en la pagina, mediante el metodo `DELETE` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.

+ `/images` : 
  - GET
    - El usuario puede obtener todas las fotos de los productos de la aplicacion en la pagina, mediante el metodo `GET` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.

+ `/products/<product_id>/images`
  -POST:
    - El usuario puede poner o crear las imagenes del producto seleccionado en la aplicacion mediante el metodo `POST` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.
+ `/images/<image_id>`
  - DELETE:
    - El usuario puede eliminar o borrar las imagenes del producto seleccionado en la aplicacion mediante el metodo `DELETE` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.
  - PATCH:
    - El usuario puede modificar las imagenes del producto seleccionado en la aplicacion mediante el metodo `PATCH` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.
+ `/comments` : 
  + GET :
    - El usuario puede ver los comentarios de cada articulo o producto mostrado en la aplicacion web mediante el metodo `GET` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.
+ `/comment/<comment_id>`
  + PATCH :
    - El usuario puede modificar cosas en su comentario hecho en una publicacion de un producto mediante el metodo `PATCH` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.
  + DELETE :
    - El usuario puede eliminar su comentario hecho en una publicacion de un producto mediante el metodo `DELETE` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.
+  `/products/<product_id>/comment`
  + POST:
    - El usuario puede crear o añadir comentarios en su propio producto o en el de otros mediante el metodo `POST` y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.  
  + 


## Hosts

Para la primera parte del desarrollo de este proyecto se utilizo unicamente un host local.

##  Forma de autenticación

La autenticacion se maneja por medio de `flask_login`.

Se implemento un modelo `Usuario` con todos los atributos requeridos para registrar un usuario.

Ademas, cabe destacar que las claves se almacenan encriptadas.

## Manejo de errores HTTP

+ 500 : Errores en el Servidor
    + Los errores en el servidor redireccionan automaticamente al usuario a la pagina principal, notificando al usuario de que ha ocurrido un error por medio de un mensaje.
+ 400 : Errores en el Cliente
  + Los errores en el cliente muestran una notificacion al usuario de que ha ocurrido un error.
+ Los codigos 100, 200 y 300 solo se utilizan para verificacion, no se notifican al usuario.

## Cómo ejecutar el sistema (Deployment scripts)

Para usuarios de Windows:

Primero se debe crear el archivo `.env` con los valores de `SECRET_KEY` y `UPLOAD_FOLDER`.

`source venv/bin/activate`

`python app.py`

Para usuarios de Linux:

`./run.sh`

## Manejo de test

Para saber que nuestra aplicacion web funciona correctamente, y nuestros endpoints hacen cada rol, y transmiten el mensaje correcto cuando hay un error o no.

+ Para la prueba de los test, se evaluo todos los endpoints con su metodo con sus casos exitosos y los fallidos

+ En cada prueba se verifico el mensaje y el codigo http recibido de los test 

+ Todos los test son satisfactorios y corren de manera correcta verificando la efectividad de los endpoints

Para usuarios de Linux:

`./test.sh`