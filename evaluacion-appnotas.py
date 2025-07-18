tareas = [{"nombre": "Estudiar documentación", "estado": False}, {"nombre": "Hacer actividad de portafolio", "estado": False}, {"nombre": "Alimentar a Titto el Gatito Gordito", "estado": True}]

def agregarTarea(tarea):
    tareaAAgregar = {"nombre": tarea, "estado": False}
    tareas.append(tareaAAgregar)

def listarTareas():
    ancho = 65
    print("************** Lista de tareas **************")
    for i, tarea in enumerate(tareas):
        estadoTarea = "Completada" if tarea["estado"] else "Pendiente"
        relleno = "." * max(0, ancho - len(tarea["nombre"]) - len(estadoTarea))
        print(f'{i + 1}. {tarea["nombre"]}{relleno}{estadoTarea}')


def marcarTarea(indice):
    indice -= 1
    tareas[indice]["estado"] = not tareas[indice]["estado"]

def eliminarTarea(indice):
    tareas.pop(indice-1)

#  Programa

opcion = 0
mensajeErrorInput = "*************Debe seleccionar una opción válida*************"

print("¡Bienvenid@ al Gestor de Tareas!")
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
        if opcion < 1 or opcion > 5:
            print(mensajeErrorInput)
            opcion = 0
    except ValueError:
        print(mensajeErrorInput)
        opcion = 0
    if opcion == 1:
        tarea = input("Ingrese el nombre de la tarea: ")
        if tarea:
            agregarTarea(tarea)
            print(f"¡'{tarea}' agregada exitosamente!")
        else:
            print("La tarea no puede estar vacía.")
    if opcion == 2:
        listarTareas()
    if opcion == 3:
        listarTareas()
        try:
            indice = int(input("Ingrese el número de la tarea a completar o dejar pendiente: "))
            if indice < 1 or indice > len(tareas):
                print(mensajeErrorInput)
            else:
                marcarTarea(indice)
                listarTareas()
        except ValueError:
            opcion = 0
            print(mensajeErrorInput)
    if opcion == 4:
        listarTareas()
        try:
            indice = int(input("Ingrese el número de la tarea a eliminar: "))
            if indice < 1 or indice > len(tareas):
                print(mensajeErrorInput)
            else:
                tareaAEliminar = tareas[indice - 1]["nombre"]
                eliminarTarea(indice)
                print(f"¡'{tareaAEliminar}' eliminada exitosamente!")
        except ValueError:
            opcion = 0
            print(mensajeErrorInput)
    if opcion == 5:
        break

print("¡Gracias por utilizar el Gestor de tareas! ¡Hasta pronto!")