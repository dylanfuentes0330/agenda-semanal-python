from pendiente import Pendiente

class Evento(Pendiente):
    def __init__(self, nombre, hora, descripcion):
        super().__init__(nombre, hora)
        self.descripcion = descripcion

    def mostrar(self):
         print(f"{self.hora} - {self.nombre} ({self.descripcion})")