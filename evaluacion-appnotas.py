tareas = [{"nombre": "Estudiar documentación", "estado": False}, {"nombre": "Hacer actividad de portafolio", "estado": False}, {"nombre": "Alimentar a Titto el Gatito Gordito", "estado": True}]

def agregarTarea(tarea):
    tareaAAgregar = {"nombre": tarea, "estado": False}
    tareas.append(tareaAAgregar)

def listarTareas():
    ancho = 65
    print("************** Lista de tareas **************")
    for i, tarea in enumerate(tareas):
        estadoTarea = "Completada" if tarea["estado"] else "Pendiente"
        relleno = "." * (ancho - len(tarea["nombre"]) - len(estadoTarea))
        print(f'{i + 1}. {tarea["nombre"]}{relleno}{estadoTarea}')


def marcarTarea(indice):
    indice -= 1
    tareas[indice]["estado"] = not tareas[indice]["estado"]

def eliminarTarea(indice):
    tareas.pop(indice-1)

#  Programa

opcion = 0



while True:
    print("""
          --- Gestor de Tareas ---
          1. Agregar tarea
          2. Ver tareas
          3. Marcar tarea como Completada/Pendiente
          4. Eliminar tarea
          5. Salir""")
    try:
        opcion = int(input("Elige una opción: "))
    except:
        print("*************Debe seleccionar una opción válida*************")
    if opcion == 1:
        tarea = input("Ingrese el nombre de la tarea")
        agregarTarea(tarea)
        print(f"¡'{tarea} agregada exitosamente!'")
    if opcion == 2:
        listarTareas()
    if opcion == 3:
        listarTareas()
        indice = int(input("Ingrese el número de la tarea a completar o dejar pendiente: "))
        marcarTarea(indice)
        listarTareas()
    if opcion == 4:
        listarTareas()
        indice = int(input("Ingrese el número de la tarea a eliminar: "))
        tareaAEliminar = tareas[indice]["nombre"]
        eliminarTarea(indice)
        print(f"¡'{tareaAEliminar}' eliminada exitosamente!")
    if opcion == 5:
        break

print("¡Gracias por utilizar el Gestor de tareas! ¡Hasta pronto!")