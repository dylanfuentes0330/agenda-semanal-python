# Agenda Semanal en Python

## Introducción

Este proyecto consiste en una agenda semanal desarrollada en Python utilizando programación orientada a objetos.

El sistema permite:
- agregar tareas
- agregar eventos
- agregar actividades
- mostrar días
- mostrar semana
- eliminar elementos

---

## Problema Identificado

Muchas personas tienen dificultades para organizar sus tareas, eventos y actividades de manera ordenada.

---

## Solución Propuesta

Se desarrolló una agenda semanal interactiva en Python que permite gestionar información organizada por días de la semana mediante un menú interactivo.

---

## Objetivos Específicos

- Aplicar clases y objetos.
- Implementar herencia.
- Aplicar polimorfismo.
- Utilizar listas.
- Implementar validaciones.
- Diseñar un menú interactivo.
- Organizar el proyecto modularmente.

---

## Tecnologías Utilizadas

- Python
- Visual Studio Code
- Programación Orientada a Objetos

---

## Conceptos Aplicados

### Herencia

Las clases Tarea, Evento y Actividad heredan de la clase Pendiente para reutilizar atributos comunes.

### Polimorfismo

Cada clase implementa su propio método mostrar().

### Modularidad

El proyecto fue dividido en varios archivos para mantener una estructura organizada.

### Validaciones

Se implementaron validaciones para:
- campos vacíos
- formato de hora
- opciones inválidas

---

## Estructura del Proyecto

```plaintext
main.py
agenda.py
dia.py
pendiente.py
tarea.py
evento.py
actividad.py
```

---

## Funcionamiento del Sistema

El sistema permite:

- agregar tareas
- agregar eventos
- agregar actividades
- mostrar días
- mostrar semana
- eliminar tareas
- eliminar eventos
- eliminar actividades

---

## Cómo Ejecutar

```bash
python main.py
```

---

## Diagrama de Clases

El sistema utiliza herencia entre las clases:

- Pendiente
- Tarea
- Evento
- Actividad

La clase Agenda administra objetos Día.

---

## Conclusiones

Este proyecto permitió aplicar conceptos importantes de programación orientada a objetos como clases, objetos, herencia, polimorfismo, listas, modularidad y validaciones, desarrollando una agenda semanal funcional e interactiva.

## Presentación

- Presentación PDF disponible en la carpeta documentacion
- Presentación Canva: https://canva.link/bgur9x6uxuyzyu2
