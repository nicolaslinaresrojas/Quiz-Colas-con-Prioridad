
# Quiz Colas con Prioridad

Nicolas Linares Rojas - 2230027

Para este programa, debemos tener en cuenta que en cada llamada se recibe en un orden de llegada y es atendida por un operador disponible, pero su solicitud es atendida por una unidad de la policía dependiendo de una clasificación establecida según su prioridad.

Para el servicio de la policía X, se elaboró un programa que organza una cola de prioridad para quienes van a ser atendidos por las unidades móviles. 

Cada persona que llame debe registrar:
- Nombre Completo
- Edad
- Dirección
- Motivo de la llamada
- Gravedad (Escala numérica de 1 a 5 siendo 1 la mayor gravedad)

Al ingresar al sistema, si la gravedad es igual que otra llamada, debe asignar prioridad según la edad de quien solicita asistencia así:

- Prioridad 1: niños menores de 12 años
- Prioridad 2: adultos mayores de 65 años
- Prioridad 4: demás personas

De igual manera se tiene en cuenta si la solicitud requiere de una unidad móvil motorizada (baja gravedad) o una patrulla y unidades de refuerzo (gravedad máxima).

El menu contiene:

- Ingresar Llamada (Ingresa datos del solicitante y muestra la posición en que será atendido)
- Pasar siguiente solicitud (Muestra los datos de la siguiente solicitud en ser atendido y lo saca de la cola)
- Mostrar la cola (Muestra la cola de atención en ese momento)

Para realizar este codigo tuve como base el codigo de los monticulos binarios, la clase Persona representa a un individuo, donde primero se inicializa los atributos y los muestra, despues la clase ColaPrioridad maneja la cola de las llamadas, donde contiene los metodos pedidos, el metodo ingresar_llamada permite al usuario ingresar los detalles de una nueva llamada y asigna la prioridad segun la gravedad y, en caso de gravedades iguales, segun la edad, el metodo siguiente_solicitud saca y muestra la siguiente solicitud de la cola para ser atendida, el metodo mostrar_cola muestra la cola actual con sus datos y al final se crea el menu. Es muy importante entender que en estos metodos nombrados anteriormente hice uso de los metodos anteriormente declarados en la clase MonticuloBinario.
