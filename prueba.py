mi_lista = []

def crear_elemento(producto):

    mi_lista.append(producto)

    print(f"Dato '{producto}' agregado correctamente.")

def mostrar_elementos():

    if mi_lista:

        for i, producto in enumerate(mi_lista, start=1):

            print(f"{i}. {producto}")

    else:

        print("La lista está vacía.")

def actualizar_elemento(indice, nuevo_valor):

    if 0 <= indice < len(mi_lista):

        mi_lista[indice] = nuevo_valor
        print(f"Dato actualizado correctamente.")

    else:

        print("No se pudo actualizar el dato.")

def eliminar_producto(indice):

    if 0 <= indice < len(mi_lista):

        producto_eliminado = mi_lista.pop(indice)
        print(f"Elemento '{producto_eliminado}' eliminado correctamente.")
    else:

        print("No se pudo eliminar el dato.")

while True:

    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        producto = input("Ingrese el producto que desea agregar: ")
        crear_elemento(producto)

    elif opcion == "2":

        mostrar_elementos()

    elif opcion == "3":

        indice = int(input("Ingrese el índice del producto que desea actualizar: "))
        nuevo_valor = input("Ingrese el nuevo valor: ")
        actualizar_elemento(indice, nuevo_valor)

    elif opcion == "4":

        indice = int(input("Ingrese el índice del producto que desea eliminar: "))
        eliminar_producto(indice)

    elif opcion == "5":

        break
    else:

        print("Error, seleccione una opción válida.")