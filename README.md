# Tarea2SD

<h3 align="Center"> Apache Kafka </h3>

_Proyecto donde se trabaja con kafka y python_

---------------------------------------

Para iniciar la aplicación, es necesario ejecutar los siguientes comandos, sin embargo para que funcionen debemos estar en la raíz de la carpeta:

<h4> Comandos </h4>

```
$ docker-compose build --no-cache
$ docker-compose up --force-recreate
```

Una vez levantado el servicio hay que ir al CLI de Kafka y ejecutar el siguiente comando para crear el topic a utilizar:
```
kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic test

```
Una vez inicializado el sistema se podran realizar las consultas al cliente, pero antes es importante acceder a la siguiente dirección, la idea de esto es que el consumer este escuchando las solicitudes realizadas: 

```
http://localhost:5000/
http://localhost:5000/blocked
```
Para poder realizar las consultas se utiliza la siguiente ruta:

```
http://localhost:8000/
http://localhost:8000/login
```
Se puede utilizar postman o el mismo navegador para probar el funcionamiento de la aplicación. En caso de postman se debe realizar una solicitud POST desde el apartado "Body", seleccionando "form-data" a la dirección del login.

---------------------------------------
<h3 align="Center">Observaciones</h3>

Para la que se este realizando constantemente la solicitud del "Consumer, se utiliza la siguiente etiqueta HTML la cual nos permite mantener actualizando constantemente la página y mantiendo el estado de espera por el flujo de datos:

```html
<head>
  <meta http-equiv="refresh" content="1">
</head>
```

---------------------------------------

<h3 align="Center">Preguntas</h3>

<p> ¿Por qué Kafka funciona bien en este escenario? </p>
Kafka trabaja con flujos de datos, es por ello que gracias a su manera asincrónica de trabajar evita que se generen aglomeraciones de estos flujos antes mencionados, que en el caso de la tarea realizada solventa perfectamente los problemas que pueden traer los login.
<br>
<br>
<p> Basado en las tecnologías que usted tiene a su disposición (Kafka, backend) ¿Qué haría usted para manejar
una gran cantidad de usuarios al mismo tiempo? </p>
Además de implementar Kafka como tal, es importante manejar una mayor cantidad de "Consumers" y de "Topics" lo que permite realizar un mejor balanceo de carga tanto para el propio Kafka como para los "Consumer" que se encuentran esperando por los mensajes enviados. En este caso el intento de login por cada usuario. Además es posible la utilizar más particiones por cada topic, la idea es que exista una respuesta a fallos en caso de que la partición principal presente fallos.

---------------------------------------

<h3 align="Left">Autores</h3>

-Esteban Alarcón
-Tomás Fuentes
