# Diccionarios iniciales
Productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
Precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
Stock = {1: 50, 2: 45, 3: 30, 4: 15}

def mostrar_productos():
    print("========================================")
    print("Lista de Productos:")
    print("========================================")
    for id_producto in Productos:
        print(f"{id_producto} \t {Productos[id_producto]} \t {Precios[id_producto]} \t {Stock[id_producto]}")
    print("========================================")
def agregar_producto():
    nuevo_id = max(Productos.keys()) + 1
    nombre = input("Ingrese el nombre del nuevo producto: ").strip()
    
    # Validación del precio
    while True:
        try:
            precio = float(input("Ingrese el precio del nuevo producto (formato decimal, por ejemplo, 200.0): "))
            if precio < 0:
                print("El precio no puede ser negativo. Intente nuevamente.")
            else:
                break
        except ValueError:
            print("Formato de precio incorrecto. Debe ser un número decimal. Intente nuevamente.")
    
    # Validación de la cantidad
    while True:
        try:
            cantidad = int(input("Ingrese el stock del nuevo producto (número entero): "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente nuevamente.")
            else:
                break
        except ValueError:
            print("Formato de cantidad incorrecto. Debe ser un número entero. Intente nuevamente.")

    Productos[nuevo_id] = nombre
    Precios[nuevo_id] = precio
    Stock[nuevo_id] = cantidad

    print("Producto agregado exitosamente.")


def eliminar_producto():
    mostrar_productos()
    id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))

    if id_eliminar in Productos:
        del Productos[id_eliminar]
        del Precios[id_eliminar]
        del Stock[id_eliminar]
        print("Producto eliminado exitosamente.")
    else:
        print("ID no encontrado.")

def actualizar_producto():
    mostrar_productos()
    id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))

    #Muestreo de valores actuales del producto seleccionado
    if id_actualizar in Productos:
        nombre = input(f"Nuevo nombre (actual: {Productos[id_actualizar]}): ")
        precio = float(input(f"Nuevo precio (actual: {Precios[id_actualizar]}): "))
        cantidad = int(input(f"Nuevo stock (actual: {Stock[id_actualizar]}): "))

        Productos[id_actualizar] = nombre
        Precios[id_actualizar] = precio
        Stock[id_actualizar] = cantidad

        print("Producto actualizado exitosamente.")
    else:
        print("ID no encontrado.")

def menu():
    while True:
        mostrar_productos()
        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
        opcion = input("Elija opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            eliminar_producto()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el programa
menu()