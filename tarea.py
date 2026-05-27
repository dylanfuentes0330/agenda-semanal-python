from pendiente import Pendiente 


class Tarea(Pendiente):
    def __init__(self, nombre, descripcion, hora):
        super().__init__(nombre, hora)
        self.descripcion = descripcion
        self.estado = False
    
    def completar(self):
        self.estado = True 

    def mostrar(self):
        if self.estado:
            estado = "Completada"
        else:
            estado = "Pendiente"

        print(f"{self.hora} - {self.nombre} ({self.descripcion}) - {estado}")