class Tarea:
    def __init__(self, texto, descripcion, estado="pendiente"):
        self.texto = texto
        self.descripcion = descripcion
        self.estado = estado

def mostrar_menu():
    print("Gestión de Tareas")
    print("1. Agregar nueva tarea")
    print("2. Mostrar todas las tareas")
    print("3. Buscar tarea por título")
    print("4. Actualizar estado de tarea")
    print("5. Actualizar descripción de tarea")
    print("6. Eliminar tarea")
    print("7. Salir")

tareas = []

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "7":
        print("Saliendo del programa.")
        break

    elif opcion == "1":
        texto = input("Escribe el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        tarea = Tarea(texto, descripcion)
        tareas.append(tarea)
        print("Tarea agregada exitosamente.")

    elif opcion == "2":
        if not tareas:
            print("No hay tareas en la lista.")
        else:
            print("\n--- Lista de Tareas ---")
            for t in tareas:
                print(f"Título: {t.texto}, Descripción: {t.descripcion}, Estado: {t.estado}")

    elif opcion == "3":
        texto = input("Escribe el título de la tarea a buscar: ").strip().lower()
        encontrado = False
        for t in tareas:
            if t.texto.lower() == texto:
                print(f"Tarea encontrada - Título: {t.texto}, Descripción: {t.descripcion}, Estado: {t.estado}")
                encontrado = True
                break
        if not encontrado:
            print("Tarea no encontrada.")

    elif opcion == "4":
        texto = input("Escribe el título de la tarea a actualizar (estado): ").strip().lower()
        encontrado = False
        for t in tareas:
            if t.texto.lower() == texto:
                t.estado = "completada"
                print("Estado de la tarea actualizado a 'completada'.")
                encontrado = True
                break
        if not encontrado:
            print("Tarea no encontrada.")

    elif opcion == "5":
        texto = input("Escribe el título de la tarea a actualizar (descripción): ").strip().lower()
        encontrado = False
        for t in tareas:
            if t.texto.lower() == texto:
                nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
                t.descripcion = nueva_descripcion
                print("Descripción de la tarea actualizada.")
                encontrado = True
                break
        if not encontrado:
            print("Tarea no encontrada.")

    elif opcion == "6":
        texto = input("Escribe el título de la tarea a eliminar: ").strip().lower()
        for t in tareas:
            if t.texto.lower() == texto:
                tareas.remove(t)
                print("Tarea eliminada.")
                break
        else:
            print("Tarea no encontrada.")

    else:
        print("Opción no válida. Inténtalo de nuevo.")
