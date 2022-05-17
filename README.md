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

**Misión:**  Ser el principal portal web de compra-venta de ropa de segunda mano en Lima.

**Visión:** Lo bueno, bonito y barato al alcance de un click.

## Información  acerca de las librerías/frameworks/plugins utilizadas en Front-end, Back-end y Base de datos.

**Front-end:**

Para agilizar el desarrollo front-end se utilizo Bootstrap 5.

**Back-end:**

Para el desarrollo backend se emplearon las siguientes librerias/frameworks:
+ Flask
+ Flask SQLAlchemy
+ Flask Login
+ Flask Migrate

**Base de datos:**

Para el desarrollo de la base de datos se utilizo unicamente PostgreSQL en su version 12.9.

## El nombre del script a ejecutar para iniciar la base de datos con datos.

Se debe crear un archivo `.env` en el directorio raiz del proyecto que establezca el valor de la variable `DATABASE_URI` al *URI* de nuestra base de datos local.

## Información acerca de los API. Requests y Responses de cada endpoint utilizado en el sistema.

+ `/usuario/login`: Se puede acceder mediante `GET` o `POST`. Cuando el servidor recibe una solicitud `GET`, retorna la pagina `login.html`. En cambio, cuando se recibe un `POST`, se utiliza para iniciar la sesion del usuario en la aplicacion y retorna una respuesta al cliente el estado de la solicitud (si fue exitosa o no) y un mensaje.

+ `/usuario/logout`: Solo se accede mediante `GET`. Cierra la sesion del usuario y retorna una redireccion a la pagina de iniciar sesion.

+ `/`: Es la pagina principal de la aplicacion. Retorna el template `index.html`, sin el usuario ademas con todos los productos disponibles en la aplicacion

+ `/usuario/registrar`: Se puede acceder mediante `GET` o `POST`. Cuando el servidor recibe una solicitud `GET`, retorna la pagina `register.html`. En cambio, cuando se recibe un `POST`, se utiliza para registrar al usuario en la aplicacion. Si todo sale bien, almacena la sesion del usuario y retorna un estado exitoso. Cuando ocurre algun error en el registro, retorna un estado fallido y un mensaje.

+ `/producto/buscar`: Permite buscar un producto por su nombre. Recibe una solicitud `GET` con el parametro para la busqueda en forma de *URL query parameters*.

+ `/producto/ver/`: Se puede acceder mediante `GET`. Retorna un template con el producto actual a ver. Permite relacionar el producto con el usuario que lo vende y que este sea capaz de contactarlo con un solo click mediante el __api de *WhatsApp*__.

+ `/producto/categoria/`:  Se puede acceder mediante `GET`. Retorna un template con los productos de una categoria en especifico.

+ `/producto/talla/`: Se puede acceder mediante `GET`. Retorna un template con los productos de una talla en especifico

+ `/producto/genero/`: Se puede acceder mediante `GET`. Retorna un template con los productos de un genero en especifico

+ `/producto/ordernar/<>/ <>`: Se puede acceder mediante `GET`. Tiene 2 parametros, un criterio para filtrar los elementos, y el otro que atributo del producto (precio,nombre). Retorna en template con los productos con el criterio y el orden indicado

+ `/producto/crear`: Se puede acceder mediante `GET` o `POST`. Cuando el servidor recibe una solicitud `GET`, retorna la pagina `vender.html`. En cambio, cuando se recibe un `POST`, se utiliza para registrar un nuevo producto en la aplicacion. Se retorna al cliente una respuesta que tiene el nuevo producto creado con todos sus atributos, asi como un estado y un mensaje. Esta informacion sera utilizada posteriormente para crear las imagenes asociadas a cada producto.

+ `/producto/borrar/`: Se puede acceder mediante `GET` o `POST`  y el metodo `DELETE`. Se elimina el porducto de la base de datos, para esto, se debe estar logeado, y que el producto sea creado por el mismo usuario

+ `/producto/editar/`:  Se puede acceder mediante `GET` o `POST`. Se puede modificar la informacion del producto. Se envia una solicitud al servidor y te retorna a la pagina `editar.html`. La informacion nueva y recopilada, sera la nueva informacion del producto

+ `/usuario/comentar`: Se puede acceder mediante `GET` o `POST`. Se puede añadir comentarios. Se mandara una peticion al servidor para modificar la vista de la pagina `producto.html` y agregar el comentario

+ `/comentario/eliminar/`: Se puede acceder mediante `GET` y por le metodo `DELETE`, para eliminar el comentario del usuario, verificando si esta logeado y si el comentario es suyo

+ `/imagen/crear`: Se puede acceder mediante `POST`. Permite crear las imagenes asociadas a cada uno de los post y almacenarlas directamente en el servidor en la carpeta `static/uploaded`. Retorna una respuesta al cliente que contiene el estado de la solicitud y un mensaje.

+ `/static/uploaded/`: Permite acceder a los recursos creados por el usuario.

+ `/static/resources/`: Permite acceder a los recursos requeridos por la aplicacion.
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