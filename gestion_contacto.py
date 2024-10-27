class Contacto:
    def __init__(self,nombre,telefono):
        self.nombre = nombre
        self.telefono = telefono
def mostrar_menu():
    print("Gestion de contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contactos")
    print("4. Eliminar contactos")
    print("5. Salir")

contactos = []

while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")

    if opcion == "5":
        print("Saliendo del programa")
        break

    if opcion == "1":
        nombre  = input("Ingrese nombre: ")
        telefono = input("Ingrese el telefono: ")
        contacto = Contacto(nombre,telefono)
        contactos.append(contacto)
        print("Contacto agregado")
    elif opcion == "2":
        for c in contactos:
            print(f"nombre: {c.nombre}, telefono: {c.telefono}")
    elif opcion == "3":
        nombre = input("ingresa el nombre a buscar: ")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f"nombre: {c.nombre}, telefono: {c.telefono}")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado")
    elif opcion == "4":
        nombre = input("Ingresa el nombre a eliminar: ")
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)
                print("Contacto eliminado")
                break

    else:
        print("Opcion no valida. Intentalo de nuevo")
