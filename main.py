from funciones import *
from equipo import Equipo

equipos = []
partidos = []

while True:

    mostrar_menu()

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        registrar_equipo(equipos)

    elif opcion == "2":
        mostrar_equipos(equipos)

    elif opcion == "3":
        registrar_partido(equipos, partidos)

    elif opcion == "4":
        mostrar_tabla(equipos)

    elif opcion == "5":

        while True:

            menu_estadisticas()

            op = input("\nSeleccione una opción: ")

            if op == "1":
                estadisticas_generales(equipos)

            elif op == "2":
                estadisticas_por_equipo(equipos)

            elif op == "3":
                break

            else:
                print("Opción inválida.")

    elif opcion == "6":
        print("Hasta luego.")
        break

    else:
        print("Opción inválida.")