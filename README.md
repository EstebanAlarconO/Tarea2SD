# Tarea2SD

kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic test

---------------------------------------

<h3 align="Center">Preguntas</h3>

<p> ¿Por qué Kafka funciona bien en este escenario? </p>
Kafka trabaja con flujos de datos, es por ello que gracias a su manera asincrónica de trabajar evita que se generen aglomeraciones de estos flujos antes mencionados, que en el caso de la tarea realizada solventa perfectamente los problemas que pueden traer los login.\



<p> Basado en las tecnologías que usted tiene a su disposición (Kafka, backend) ¿Qué haría usted para manejar
una gran cantidad de usuarios al mismo tiempo? </p>
Además de implementar Kafka como tal, es importante manejar una mayor cantidad de "Consumers" y de "Topics" lo que permite realizar un mejor balanceo de carga tanto para el propio Kafka como para los "Consumer" que se encuentran esperando por los mensajes enviados. En este caso el intento de login por cada usuario. Además es posible la utilizar más particiones por cada topic, la idea es que exista una respuesta a fallos en caso de que la partición principal presente fallos.

---------------------------------------

<h3 align="Left">Autores</h3>

-Esteban Alarcón
-Tomás Fuentes
