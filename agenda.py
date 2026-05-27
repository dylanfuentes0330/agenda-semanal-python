from dia import Dia 

class Agenda: 
    def __init__(self):
        self.dias = []
        self.inicializar_semana()
    
    def inicializar_semana(self):
        nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        for nombre in nombres_dias:
            self.dias.append(Dia(nombre))
    
    def seleccionar_dia(self, nombre):
        for dia in self.dias:
            if dia.nombre.lower() == nombre.lower():
                return dia
        
        print("Día no encontrado")
        return None
    
    def mostrar_semana(self):
        print("\nAgenda Semanal:")
        
        for dia in self.dias:
            dia.mostrar_dia()

    