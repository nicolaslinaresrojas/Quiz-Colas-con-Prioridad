
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

Para realizar este codigo me guie principalmente en los monticulos, donde primero establecí la clase MonticuloBinario donde declaré los metodos de este para posteriormente crear otra clase con nombre Llamada, en este declaré las prioridades de las gravedades y los datos a pedir, los cuales son: nombre, edad, direccion, motivo y gravedad. Como siguiente paso cree la clase ColaPrioridad, la cual contiene los metodos pedidos, y en cada uno de estos hice uso de los metodos que establecí en la clase MonticuloBinario, y finalmente cree el menu con su respectiva informacion.