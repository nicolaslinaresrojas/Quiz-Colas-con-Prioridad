class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = []
        self.tamanoActual = 0
        
    def infiltArriba(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
                i = i // 2

    def insertar(self, llamada):
        self.listaMonticulo.append(llamada)
        self.tamanoActual += 1
        self.infiltArriba(self.tamanoActual)
        
    def infiltAbajo(self, i):
        while (i * 2) <= self.tamanoActual:
            hijoMin = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[hijoMin][0]:
                self.listaMonticulo[i], self.listaMonticulo[hijoMin] = self.listaMonticulo[hijoMin], self.listaMonticulo[i]
                i = hijoMin
                
    def hijoMin(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2][0] < self.listaMonticulo[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual -= 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

class Llamada:
    
    def __init__(self, nombre, edad, direccion, motivo, gravedad):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.motivo = motivo
        self.gravedad = gravedad
    
    def __lt__(self, other):
        if self.gravedad == other.gravedad:
            if self.edad < 12:
                return True
            elif self.edad >= 65:
                return False
            elif other.edad < 12:
                return False
            elif other.edad >= 65:
                return True
            else:
                return False
        else:
            return self.gravedad < other.gravedad
        
class ColaPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()
                
    def ingresar_llamada(self, llamada):
        self.monticulo.insertar(llamada)
        print("Llamada ingresada. Posición en la cola:", self.monticulo.tamanoActual)
        
    def pasar_siguiente_solicitud(self):
        if self.monticulo.tamanoActual > 0:
            llamada = self.monticulo.eliminarMin()
            print("Siguiente solicitud a ser atendida:")
            print("Nombre:", llamada.nombre)
            print("Edad:", llamada.edad)
            print("Direccion:", llamada.direccion)
            print("Motivo:", llamada.motivo)
            print("Gravedad:", llamada.gravedad)
        else:
            print("No hay solicitudes pendientes.")
            
    def mostrar_cola(self):
        print("Cola de atención en este momento:")
        for i in range(1, self.monticulo.tamanoActual + 1):
            llamada = self.monticulo.listaMonticulo[i]
            print("Posicion:", i)
            print("Nombre:", llamada.nombre)
            print("Edad:", llamada.edad)
            print("Direccion:", llamada.direccion)
            print("Motivo:", llamada.motivo)
            print("Gravedad:", llamada.gravedad)
            
def menu():
        print("\nMenú:")
        print("1. Ingresar Llamada")
        print("2. Pasar siguiente solicitud")
        print("3. Mostrar la cola")
        print("4. Salir")
        
cola_prioridad = ColaPrioridad()

while True:
    
    menu()
    opcion = input("Seleccione una opción: ")
        
    if opcion == "1":
            
            nombre = input("Ingrese nombre completo: ")
            edad = int(input("Ingrese edad: "))
            direccion = input("Ingrese direccion: ")
            motivo = input("Ingrese motivo de la llamada: ")
            gravedad = int(input("Ingrese gravedad (1-5): "))
            llamada = Llamada(nombre, edad, direccion, motivo, gravedad)
            cola_prioridad.ingresar_llamada(llamada)
            
    elif opcion == "2":
        cola_prioridad.pasar_siguiente_solicitud()
    elif opcion == "3":
        cola_prioridad.mostrar_cola()
    elif opcion == "4":
        print("Saliendo")
        break
    else:
        print("Opcion Invalida")
