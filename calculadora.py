def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    if b != 0:
        return a/ b
    else:
        return "error: division por cero"

def mostrar_menu():
    print("Calculadora básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Saliendo del programa.")
        break

    if opcion in ["1","2","3","4"]:
        num1 = float(input("Ingresa el primer número"))
        num2 = float(input("Ingresa el segundo número"))

        if opcion == "1":
            print(f"Resultado es: {suma(num1,num2)}")
        elif opcion == "2":
            print(f"Resultado es: {resta(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado es: {mult(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado es: {div(num1, num2)}")
    else:
        print("Opcion no valida, intentar de nuevo.")