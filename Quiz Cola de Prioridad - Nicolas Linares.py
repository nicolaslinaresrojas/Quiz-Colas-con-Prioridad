# Nicolas Linares 2230027 - Quiz Monticulos

class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0


    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2

    def insertar(self,k):
      self.listaMonticulo.append(k)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self,i):
      while (i * 2) <= self.tamanoActual:
          hm = self.hijoMin(i)
          if self.listaMonticulo[i] > self.listaMonticulo[hm]:
              tmp = self.listaMonticulo[i]
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual:
          return i * 2
      else:
          if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def eliminarMin(self):
      valorSacado = self.listaMonticulo[1]
      self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
      self.tamanoActual = self.tamanoActual - 1
      self.listaMonticulo.pop()
      self.infiltAbajo(1)
      return valorSacado

    def construirMonticulo(self,unaLista):
      i = len(unaLista) // 2
      self.tamanoActual = len(unaLista)
      self.listaMonticulo = [0] + unaLista[:]
      while (i > 0):
          self.infiltAbajo(i)
          i = i - 1

class Persona:
    def __init__(self, nombre, edad, direccion, motivo, gravedad):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.motivo = motivo
        self.gravedad = gravedad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Direccion: {self.direccion}, Motivo: {self.motivo}, Gravedad: {self.gravedad}"

class ColaPrioridad:
    def __init__(self):
        self.cola = MonticuloBinario()

    def ingresar_llamada(self):
        nombre = input("Ingresa el nombre: ")
        edad = int(input("Ingresa la edad: "))
        direccion = input("Ingresa la direccion: ")
        motivo = input("Ingresa el motivo de la llamada: ")
        gravedad = int(input("Ingresa la gravedad del 1 al 5: "))

        gravedades = [llamada[1] for llamada in self.cola.listaMonticulo[1:]]
        if gravedad in gravedades:
            if edad < 12:
                prioridad = 1
            elif edad >= 65:
                prioridad = 2
            else:
                prioridad = 4
        else:
            if edad < 12:
                prioridad = 1
            elif edad >= 65:
                prioridad = 2
            else:
                prioridad = 4

        persona = Persona(nombre, edad, direccion, motivo, gravedad)
        self.cola.insertar((prioridad, gravedad, persona))

        print(f"{persona.nombre} fue añadida a la cola con prioridad {prioridad}.")

    def siguiente_solicitud(self):
        if self.cola.tamanoActual == 0:
            print("No hay solicitudes en la cola")
            return

        siguiente = self.cola.eliminarMin()
        print("Siguiente solicitud a atender:")
        print(siguiente[2]) 
        print(f"Prioridad: {siguiente[0]}, Gravedad: {siguiente[1]}")

    def mostrar_cola(self):
        if self.cola.tamanoActual == 0:
            print("La cola no existe")
            return

        print("Cola de atencion:")
        for i in range(1, self.cola.tamanoActual + 1):
            print(f"{i}. {self.cola.listaMonticulo[i][2]} - Prioridad: {self.cola.listaMonticulo[i][0]}, Gravedad: {self.cola.listaMonticulo[i][1]}")


cola_prioridad = ColaPrioridad()

while True:
    print("\nMenú:")
    print("1) Ingresar Nueva Llamada")
    print("2) Pasar siguiente solicitud")
    print("3) Mostrar cola")
    print("4) Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cola_prioridad.ingresar_llamada()
    elif opcion == "2":
        cola_prioridad.siguiente_solicitud()
    elif opcion == "3":
        cola_prioridad.mostrar_cola()
    elif opcion == "4":
        print("Saliendo")
        break
    else:
        print("Opcion no valida")
