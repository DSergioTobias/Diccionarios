diccionario = {
    1: {
        "id": 2003,
        "nombre": "alex",
        "apellido": "gomez",
        "edad": 23,
    },
    2: {
        "id": 2004,
        "nombre": "sergio",
        "apellido": "tobias",
        "edad": 22,
    },
    3: {
        "id": 2005,
        "nombre": "sebastian",
        "apellido": "rodriquez",
        "edad": 21,
    }
}

salir = False
while not salir:
    print("\n1. Agregar")
    print("2. Eliminar")
    print("3. Actualizar")
    print("4. Mostrar")
    print("5. Salir")

    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Error: Debes ingresar un número entero.")
        continue

    # ── AGREGAR ──────────────────────────────────────────────────────────────
    if opcion == 1:
        try:
            input_id       = int(input("Ingrese el id: "))
            input_nombre   = input("Ingrese el nombre: ")
            input_apellido = input("Ingrese el apellido: ")
            input_edad     = int(input("Ingrese la edad: "))

            nueva_clave = max(diccionario.keys()) + 1 if diccionario else 1
            diccionario[nueva_clave] = {
                "id":       input_id,
                "nombre":   input_nombre,
                "apellido": input_apellido,
                "edad":     input_edad,
            }
            print("Registro agregado:", diccionario[nueva_clave])
        except ValueError:
            print("Error: El id y la edad deben ser números enteros.")

    # ── ELIMINAR ─────────────────────────────────────────────────────────────
    elif opcion == 2:
        while True:
            print("\n1. Eliminar diccionario completo")
            print("2. Eliminar un registro por clave")
            print("3. Eliminar un campo de un registro")
            print("4. Volver al menú principal")

            try:
                sub_opcion = int(input("Elige una opción: "))
            except ValueError:
                print("Error: Debes ingresar un número entero.")
                continue

            if sub_opcion == 1:
                diccionario.clear()
                print("Diccionario eliminado:", diccionario)

            elif sub_opcion == 2:
                try:
                    print("Claves disponibles:", list(diccionario.keys()))
                    clave = int(input("Ingrese la clave del registro a eliminar: "))
                    if clave in diccionario:
                        del diccionario[clave]
                        print(f"Registro {clave} eliminado.")
                    else:
                        print("Error: Clave no encontrada.")
                except ValueError:
                    print("Error: La clave debe ser un número entero.")

            elif sub_opcion == 3:
                try:
                    print("Claves disponibles:", list(diccionario.keys()))
                    clave = int(input("Ingrese la clave del registro: "))
                    if clave in diccionario:
                        while True:
                            print("\n1. Eliminar id")
                            print("2. Eliminar nombre")
                            print("3. Eliminar apellido")
                            print("4. Eliminar edad")
                            print("5. Volver al menú anterior")

                            try:
                                sub_opcion2 = int(input("Elige una opción: "))
                            except ValueError:
                                print("Error: Debes ingresar un número entero.")
                                continue

                            campos = {1: "id", 2: "nombre", 3: "apellido", 4: "edad"}
                            if sub_opcion2 in campos:
                                campo = campos[sub_opcion2]
                                if campo in diccionario[clave]:
                                    del diccionario[clave][campo]
                                    print(f"Campo '{campo}' eliminado del registro {clave}.")
                                else:
                                    print(f"Error: El campo '{campo}' no existe en ese registro.")
                            elif sub_opcion2 == 5:
                                break
                            else:
                                print("Opción inválida.")
                    else:
                        print("Error: Clave no encontrada.")
                except ValueError:
                    print("Error: La clave debe ser un número entero.")

            elif sub_opcion == 4:
                break
            else:
                print("Opción inválida.")

    # ── ACTUALIZAR ───────────────────────────────────────────────────────────
    elif opcion == 3:
        try:
            print("Claves disponibles:", list(diccionario.keys()))
            clave = int(input("Ingrese la clave del registro a actualizar: "))
            if clave in diccionario:
                while True:
                    print("\n1. Actualizar id")
                    print("2. Actualizar nombre")
                    print("3. Actualizar apellido")
                    print("4. Actualizar edad")
                    print("5. Volver al menú principal")

                    try:
                        sub_opcion = int(input("Elige una opción: "))
                    except ValueError:
                        print("Error: Debes ingresar un número entero.")
                        continue

                    if sub_opcion == 1:
                        try:
                            diccionario[clave]["id"] = int(input("Nuevo id: "))
                            print("Id actualizado.")
                        except ValueError:
                            print("Error: El id debe ser un número entero.")
                    elif sub_opcion == 2:
                        diccionario[clave]["nombre"] = input("Nuevo nombre: ")
                        print("Nombre actualizado.")
                    elif sub_opcion == 3:
                        diccionario[clave]["apellido"] = input("Nuevo apellido: ")
                        print("Apellido actualizado.")
                    elif sub_opcion == 4:
                        try:
                            diccionario[clave]["edad"] = int(input("Nueva edad: "))
                            print("Edad actualizada.")
                        except ValueError:
                            print("Error: La edad debe ser un número entero.")
                    elif sub_opcion == 5:
                        break
                    else:
                        print("Opción inválida.")
            else:
                print("Error: Clave no encontrada.")
        except ValueError:
            print("Error: La clave debe ser un número entero.")

    # ── MOSTRAR ──────────────────────────────────────────────────────────────
    elif opcion == 4:
        try:
            if diccionario:
                print("\n{:<6} {:<6} {:<12} {:<12} {:<5}".format(
                    "Clave", "ID", "Nombre", "Apellido", "Edad"))
                print("-" * 45)
                for clave, datos in diccionario.items():
                    print("{:<6} {:<6} {:<12} {:<12} {:<5}".format(
                        clave,
                        datos.get("id", "N/A"),
                        datos.get("nombre", "N/A"),
                        datos.get("apellido", "N/A"),
                        datos.get("edad", "N/A"),
                    ))
            else:
                print("El diccionario está vacío.")
        except Exception as e:
            print(f"Error inesperado al mostrar los datos: {e}")

    # ── SALIR ─────────────────────────────────────────────────────────────────
    elif opcion == 5:
        print("Saliendo del programa...")
        salir = True

    else:
        print("Opción inválida, intente de nuevo.")