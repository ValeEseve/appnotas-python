tareas = [{"nombre": "Estudiar documentación", "estado": "Pendiente"}, {"nombre": "Hacer actividad de portafolio", "estado": "Pendiente"}]

def agregarTarea(tarea):
    tareas.append(tarea)

def listarTareas():
    ancho = 40
    for tarea in tareas:
        relleno = "." * (ancho - len(tarea.nombre) - len(tarea.estado))
        print(f'{tarea.nombre}{relleno}{tarea.estado}')