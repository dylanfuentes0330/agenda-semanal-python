from tarea import Tarea
from evento import Evento
from actividad import Actividad

class Dia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []
        self.eventos = []
        self.actividades = []
    
    def agregar_tarea(self, tarea):
        for t in self.tareas:
            if t.nombre == tarea.nombre:
                print("La tarea ya existe")
                return

        self.tareas.append(tarea)
        print("Tarea agregada correctamente")
    
    def eliminar_tarea(self, nombre):
        encontrada = False

        for t in self.tareas:
            if t.nombre == nombre:
                encontrada = True

        if not encontrada:
          print("La tarea no existe")
        else:
            self.tareas = [t for t in self.tareas if t.nombre != nombre]
            print("Tarea eliminada")
    
    def agregar_evento(self, evento):
         for e in self.eventos:
            if e.nombre == evento.nombre:
                print("El evento ya existe")
                return

         self.eventos.append(evento)
         print("Evento agregado correctamente")
    
    def eliminar_evento(self,nombre):
        encontrada = False

        for e in self.eventos:
            if e.nombre == nombre:
                encontrada = True

        if not encontrada:
          print("El evento no existe")
        else:
            self.eventos = [e for e in self.eventos if e.nombre != nombre]
            print("Evento eliminado")
    
    def agregar_actividad(self, actividad):
        for a in self.actividades:
          if a.nombre == actividad.nombre:
                print("La actividad ya existe")
                return

        self.actividades.append(actividad)
        print("Actividad agregada correctamente")
    
    
    def eliminar_actividad(self,nombre):
         encontrada = False

         for a in self.actividades:
            if a.nombre == nombre:
                encontrada = True

         if not encontrada:
            print("La actividad no existe")
         else:
            self.actividades = [a for a in self.actividades if a.nombre != nombre]
            print("Actividad eliminada")

    def ordenar_por_hora(self):
        self.tareas.sort(key=lambda x: x.hora)
        self.eventos.sort(key=lambda x: x.hora)
        self.actividades.sort(key=lambda x: x.hora)     

    def mostrar_dia(self):
        self.ordenar_por_hora()
        print("\nDia:", self.nombre)

        print("Tareas:")
        if not self.tareas:
            print("No hay tareas")
        else:
            for tarea in self.tareas:
                tarea.mostrar()

        print("Eventos:")
        if not self.eventos:
            print("No hay eventos")
        else:
            for evento in self.eventos:
                evento.mostrar()

        print("Actividades:")
        if not self.actividades:
            print("No hay actividades")
        else:
            for actividad in self.actividades:
                actividad.mostrar()
        
  