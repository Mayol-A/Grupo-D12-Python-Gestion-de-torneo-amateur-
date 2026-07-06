from equipo import Equipo
MAX_EQUIPOS = 16

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

def buscar_partido(partidos, fecha, equipo1, equipo2):

    for partido in partidos:

        if partido["fecha"] == fecha:

            if (partido["equipo1"].lower() == equipo1.lower() and
                partido["equipo2"].lower() == equipo2.lower()) or \
                (partido["equipo1"].lower() == equipo2.lower() and
                partido["equipo2"].lower() == equipo1.lower()):

                return True

    return False

def registrar_equipo(equipos):

    if len(equipos) >= MAX_EQUIPOS:
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
    print(f"Equipos registrados: {len(equipos)}/{MAX_EQUIPOS}")


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

    if len(equipos) < 2:
        print("\nSe necesitan al menos dos equipos registrados.")
        return

    try:
        fecha = int(input("\nIngrese la fecha del partido: "))
    except ValueError:
        print("La fecha debe ser un número.")
        return

    equipo1 = input("Ingrese el primer equipo: ").strip()
    equipo2 = input("Ingrese el segundo equipo: ").strip()

    if equipo1.lower() == equipo2.lower():
        print("Un equipo no puede jugar contra sí mismo.")
        return

    equipo_local = buscar_equipo(equipos, equipo1)
    equipo_visitante = buscar_equipo(equipos, equipo2)

    if equipo_local is None or equipo_visitante is None:
        print("Uno o ambos equipos no están registrados.")
        return

    if buscar_partido(partidos, fecha, equipo1, equipo2):
        print("Ese partido ya fue registrado para esa fecha.")
        return

    try:
        goles1 = int(input(f"Goles de {equipo1}: "))
        goles2 = int(input(f"Goles de {equipo2}: "))
    except ValueError:
        print("Los goles deben ser números.")
        return

    if goles1 < 0 or goles2 < 0:
        print("Los goles no pueden ser negativos.")
        return

    penales1 = 0
    penales2 = 0

    if goles1 == goles2:

        respuesta = input("¿Hubo definición por penales? (S/N): ").upper()

        if respuesta == "S":

            try:
                penales1 = int(input(f"Penales convertidos por {equipo1}: "))
                penales2 = int(input(f"Penales convertidos por {equipo2}: "))
            except ValueError:
                print("Los penales deben ser números.")
                return
            
            if penales1 < 0 or penales2 < 0:
                print("Los penales no pueden ser negativos.")
                return

            equipo_local.penales_convertidos += penales1
            equipo_visitante.penales_convertidos += penales2

    partido = {
        "fecha": fecha,
        "equipo1": equipo1,
        "equipo2": equipo2
    }

    partidos.append(partido)

    equipo_local.pj += 1
    equipo_visitante.pj += 1

    equipo_local.gf += goles1
    equipo_local.gc += goles2

    equipo_visitante.gf += goles2
    equipo_visitante.gc += goles1

    if goles1 > goles2:

        equipo_local.pg += 1
        equipo_visitante.pp += 1

        equipo_local.pts += 3

    elif goles2 > goles1:

        equipo_visitante.pg += 1
        equipo_local.pp += 1

        equipo_visitante.pts += 3

    else:

        equipo_local.pe += 1
        equipo_visitante.pe += 1

        equipo_local.pts += 1
        equipo_visitante.pts += 1

    equipo_local.dg = equipo_local.gf - equipo_local.gc
    equipo_visitante.dg = equipo_visitante.gf - equipo_visitante.gc

    print("\nPartido registrado correctamente.")


def mostrar_tabla(equipos):
    print("Función en desarrollo...")


def estadisticas_generales(equipos):
    print("Función en desarrollo...")


def estadisticas_por_equipo(equipos):
    print("Función en desarrollo...")