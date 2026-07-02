from equipo import Equipo

def mostrar_menu():
    print("\n========== TORNEO AMATEUR ==========")
    print("1. Registrar equipo")
    print("2. Mostrar equipos")
    print("3. Registrar partido")
    print("4. Tabla de posiciones")
    print("5. Estadísticas")
    print("6. Salir")


def menu_estadisticas():
    print("\n======= ESTADÍSTICAS =======")
    print("1. Estadísticas generales")
    print("2. Estadísticas por equipo")
    print("3. Volver")

def buscar_equipo(equipos, nombre):

    for equipo in equipos:

        if equipo.nombre.lower() == nombre.lower():
            return equipo

    return None

def registrar_equipo(equipos):

    if len(equipos) >= 16:
        print("\nNo se pueden registrar más de 16 equipos.")
        return

    while True:

        nombre = input("\nIngrese el nombre del equipo: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue

        if buscar_equipo(equipos, nombre):

            print("Ese equipo ya está registrado.")
            continue

        break

    nuevo = Equipo(nombre)

    equipos.append(nuevo)

    print(f"\nEquipo '{nombre}' registrado correctamente.")

def mostrar_equipos(equipos):

    if len(equipos) == 0:
        print("\nNo hay equipos registrados.")
        return

    print("\n====== EQUIPOS REGISTRADOS ======\n")

    contador = 1

    for equipo in equipos:

        print(f"{contador}. {equipo.nombre}")

        contador += 1


def registrar_partido(equipos, partidos):
    print("Función en desarrollo...")


def mostrar_tabla(equipos):
    print("Función en desarrollo...")


def estadisticas_generales(equipos):
    print("Función en desarrollo...")


def estadisticas_por_equipo(equipos):
    print("Función en desarrollo...")