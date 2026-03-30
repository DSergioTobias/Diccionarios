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

# ── UTILIDAD ──────────────────────────────────────────────────────────────────
def pedir_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print("Error: Debes ingresar un número entero.")
        return None

def pedir_clave(diccionario):
    print("Claves disponibles:", list(diccionario.keys()))
    clave = pedir_entero("Ingrese la clave del registro: ")
    if clave is None:
        return None
    if clave not in diccionario:
        print("Error: Clave no encontrada.")
        return None
    return clave

# ── AGREGAR ───────────────────────────────────────────────────────────────────
def agregar(diccionario):
    try:
        input_id       = pedir_entero("Ingrese el id: ")
        if input_id is None: return
        input_nombre   = input("Ingrese el nombre: ")
        input_apellido = input("Ingrese el apellido: ")
        input_edad     = pedir_entero("Ingrese la edad: ")
        if input_edad is None: return

        nueva_clave = max(diccionario.keys()) + 1 if diccionario else 1
        diccionario[nueva_clave] = {
            "id":       input_id,
            "nombre":   input_nombre,
            "apellido": input_apellido,
            "edad":     input_edad,
        }
        print("Registro agregado:", diccionario[nueva_clave])
    except Exception as e:
        print(f"Error inesperado al agregar: {e}")

# ── ELIMINAR ──────────────────────────────────────────────────────────────────
def eliminar_todo(diccionario):
    diccionario.clear()
    print("Diccionario eliminado:", diccionario)

def eliminar_registro(diccionario):
    clave = pedir_clave(diccionario)
    if clave is None: return
    del diccionario[clave]
    print(f"Registro {clave} eliminado.")

def eliminar_campo(diccionario):
    clave = pedir_clave(diccionario)
    if clave is None: return

    while True:
        print("\n1. Eliminar id")
        print("2. Eliminar nombre")
        print("3. Eliminar apellido")
        print("4. Eliminar edad")
        print("5. Volver al menú anterior")

        sub_opcion = pedir_entero("Elige una opción: ")
        if sub_opcion is None: continue

        campos = {1: "id", 2: "nombre", 3: "apellido", 4: "edad"}
        if sub_opcion in campos:
            campo = campos[sub_opcion]
            if campo in diccionario[clave]:
                del diccionario[clave][campo]
                print(f"Campo '{campo}' eliminado del registro {clave}.")
            else:
                print(f"Error: El campo '{campo}' no existe en ese registro.")
        elif sub_opcion == 5:
            break
        else:
            print("Opción inválida.")

def eliminar(diccionario):
    while True:
        print("\n1. Eliminar diccionario completo")
        print("2. Eliminar un registro por clave")
        print("3. Eliminar un campo de un registro")
        print("4. Volver al menú principal")

        sub_opcion = pedir_entero("Elige una opción: ")
        if sub_opcion is None: continue

        if   sub_opcion == 1: eliminar_todo(diccionario)
        elif sub_opcion == 2: eliminar_registro(diccionario)
        elif sub_opcion == 3: eliminar_campo(diccionario)
        elif sub_opcion == 4: break
        else: print("Opción inválida.")

# ── ACTUALIZAR ────────────────────────────────────────────────────────────────
def actualizar(diccionario):
    clave = pedir_clave(diccionario)
    if clave is None: return

    while True:
        print("\n1. Actualizar id")
        print("2. Actualizar nombre")
        print("3. Actualizar apellido")
        print("4. Actualizar edad")
        print("5. Volver al menú principal")

        sub_opcion = pedir_entero("Elige una opción: ")
        if sub_opcion is None: continue

        if sub_opcion == 1:
            nuevo_id = pedir_entero("Nuevo id: ")
            if nuevo_id is None: continue
            diccionario[clave]["id"] = nuevo_id
            print("Id actualizado.")
        elif sub_opcion == 2:
            diccionario[clave]["nombre"] = input("Nuevo nombre: ")
            print("Nombre actualizado.")
        elif sub_opcion == 3:
            diccionario[clave]["apellido"] = input("Nuevo apellido: ")
            print("Apellido actualizado.")
        elif sub_opcion == 4:
            nueva_edad = pedir_entero("Nueva edad: ")
            if nueva_edad is None: continue
            diccionario[clave]["edad"] = nueva_edad
            print("Edad actualizada.")
        elif sub_opcion == 5:
            break
        else:
            print("Opción inválida.")

# ── MOSTRAR ───────────────────────────────────────────────────────────────────
def mostrar(diccionario):
    try:
        if diccionario:
            print("\n{:<6} {:<6} {:<12} {:<12} {:<5}".format(
                "Clave", "ID", "Nombre", "Apellido", "Edad"))
            print("-" * 45)
            for clave, datos in diccionario.items():
                print("{:<6} {:<6} {:<12} {:<12} {:<5}".format(
                    clave,
                    datos.get("id",       "N/A"),
                    datos.get("nombre",   "N/A"),
                    datos.get("apellido", "N/A"),
                    datos.get("edad",     "N/A"),
                ))
        else:
            print("El diccionario está vacío.")
    except Exception as e:
        print(f"Error inesperado al mostrar los datos: {e}")

# ── MENÚ PRINCIPAL ────────────────────────────────────────────────────────────
def menu():
    salir = False
    while not salir:
        print("\n1. Agregar")
        print("2. Eliminar")
        print("3. Actualizar")
        print("4. Mostrar")
        print("5. Salir")

        opcion = pedir_entero("Ingrese una opcion: ")
        if opcion is None: continue

        if   opcion == 1: agregar(diccionario)
        elif opcion == 2: eliminar(diccionario)
        elif opcion == 3: actualizar(diccionario)
        elif opcion == 4: mostrar(diccionario)
        elif opcion == 5:
            print("Saliendo del programa...")
            salir = True
        else:
            print("Opción inválida, intente de nuevo.")

menu()