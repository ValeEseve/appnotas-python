tareas = [{"nombre": "Estudiar documentación", "estado": False}, {"nombre": "Hacer actividad de portafolio", "estado": False}]

def agregarTarea(tarea):
    tareas.append(tarea)

def listarTareas():
    ancho = 65
    print("************** Lista de tareas **************")
    for i, tarea in enumerate(tareas):
        estadoTarea = "Completada" if tarea["estado"] else "Pendiente"
        relleno = "." * (ancho - len(tarea["nombre"]) - len(estadoTarea))
        print(f'{i + 1}. {tarea["nombre"]}{relleno}{estadoTarea}')


def marcarCompletada(indice):
    indice -= 1
    tareas[indice]["estado"] = not tareas[indice]["estado"]



listarTareas()
marcarCompletada(1)
listarTareas()