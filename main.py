from agenda import Agenda
from tarea import Tarea
from evento import Evento
from actividad import Actividad

agenda = Agenda()

while True:
    print("\nAGENDA SEMANAL")
    print("1. Agregar tarea")
    print("2. Agregar evento")
    print("3. Agregar actividad")
    print("4. Mostrar día")
    print("5. Mostrar semana")
    print("6. Eliminar tarea")
    print("7. Eliminar evento")
    print("8. Eliminar actividad")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Opción inválida")
        continue

    # AGREGAR TAREA
    if opcion == "1":
        nombre = input("Nombre de la tarea: ")
        descripcion = input("Descripción: ")
        hora = input("Hora (HH:MM): ")
        dia_nombre = input("Día de la semana: ")

        if nombre == "" or descripcion == "" or hora == "" or dia_nombre == "":
            print("Todos los campos son obligatorios")
            continue

        if ":" not in hora or len(hora) != 5:
            print("Formato de hora inválido")
            continue

        dia = agenda.seleccionar_dia(dia_nombre)

        if dia is None:
            print("Día no válido")
            continue

        tarea = Tarea(nombre, descripcion, hora)
        dia.agregar_tarea(tarea)

    # AGREGAR EVENTO
    elif opcion == "2":
        nombre = input("Nombre del evento: ")
        descripcion = input("Descripción: ")
        hora = input("Hora (HH:MM): ")
        dia_nombre = input("Día de la semana: ")

        if nombre == "" or descripcion == "" or hora == "" or dia_nombre == "":
            print("Todos los campos son obligatorios")
            continue

        if ":" not in hora or len(hora) != 5:
            print("Formato de hora inválido")
            continue

        dia = agenda.seleccionar_dia(dia_nombre)

        if dia is None:
            print("Día no válido")
            continue

        evento = Evento(nombre, hora, descripcion)
        dia.agregar_evento(evento)

    # AGREGAR ACTIVIDAD
    elif opcion == "3":
        nombre = input("Nombre de la actividad: ")
        duracion = input("Duración en minutos: ")
        hora = input("Hora (HH:MM): ")
        dia_nombre = input("Día de la semana: ")

        if nombre == "" or duracion == "" or hora == "" or dia_nombre == "":
            print("Todos los campos son obligatorios")
            continue

        if ":" not in hora or len(hora) != 5:
            print("Formato de hora inválido")
            continue

        dia = agenda.seleccionar_dia(dia_nombre)

        if dia is None:
            print("Día no válido")
            continue

        actividad = Actividad(nombre, duracion, hora)
        dia.agregar_actividad(actividad)

    # MOSTRAR DÍA
    elif opcion == "4":
        dia_nombre = input("Ingrese el día: ")

        if dia_nombre == "":
            print("Debe ingresar un día")
            continue

        dia = agenda.seleccionar_dia(dia_nombre)

        if dia is None:
            print("Día no válido")
            continue

        dia.mostrar_dia()

    # MOSTRAR SEMANA
    elif opcion == "5":
        agenda.mostrar_semana()

   
   # ELIMINAR TAREA
    elif opcion == "6":
        dia_nombre = input("Día de la semana: ")
        nombre = input("Nombre de la tarea a eliminar: ")

        if dia_nombre == "" or nombre == "":
            print("Todos los campos son obligatorios")
            continue

        dia = agenda.seleccionar_dia(dia_nombre)

        if dia is None:
            print("Día no válido")
            continue

        dia.eliminar_tarea(nombre)

# ELIMINAR EVENTO
    elif opcion == "7":
        dia_nombre = input("Día de la semana: ")
        nombre = input("Nombre del evento a eliminar: ")

        if dia_nombre == "" or nombre == "":
            print("Todos los campos son obligatorios")
            continue

        dia = agenda.seleccionar_dia(dia_nombre)

        if dia is None:
            print("Día no válido")
            continue

        dia.eliminar_evento(nombre)

# ELIMINAR ACTIVIDAD
    elif opcion == "8":
        dia_nombre = input("Día de la semana: ")
        nombre = input("Nombre de la actividad a eliminar: ")

        if dia_nombre == "" or nombre == "":
            print("Todos los campos son obligatorios")
            continue

        dia = agenda.seleccionar_dia(dia_nombre)

        if dia is None:
            print("Día no válido")
            continue

        dia.eliminar_actividad(nombre)

 elif opcion == "9":
        dia_nombre = input("Día de la semana: ")
        nombre = input("Nombre de la tarea: ")

        dia = agenda.seleccionar_dia(dia_nombre)

        if dia is None:
            print("Día no válido")
            continue

        encontrada = False

        for tarea in dia.tareas:
            if tarea.nombre.lower() == nombre.lower():
                tarea.completar()
                encontrada = True
                print("Tarea completada")

        if not encontrada:
            print("Tarea no encontrada")

    elif opcion == "10":
        print("Saliendo del programa...")
        break
