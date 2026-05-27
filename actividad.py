from pendiente import Pendiente

class Actividad(Pendiente):
    def __init__(self, nombre, duracion, hora):
        super().__init__(nombre, hora)
        self.duracion = duracion
      
    
    def mostrar(self):
        print(self.hora, "-", self.nombre, "-", self.duracion, "min")