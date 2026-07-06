# Grupo-D12-Python-Gestion-de-torneo-amateur-
Trabajo integrador final de Python AED

# Integrantes:
  Alavarado Rolón Analuz Agustina,
  Lezcano Olmedo Liz Rebeca,
  Mayol Ana Paula

# Comisión: K1.4


# Descripción General del Sistema

  ## Descripción general

El Sistema de Gestión de Torneo Amateur es una aplicación desarrollada en Python que funciona mediante consola y tiene como objetivo administrar un torneo de fútbol amateur de forma sencilla e intuitiva.

El sistema permite registrar hasta 16 equipos participantes, gestionar los partidos disputados entre ellos y generar automáticamente la tabla de posiciones siguiendo las reglas oficiales del fútbol.

Además, ofrece un módulo de estadísticas que permite consultar información general del torneo y estadísticas individuales de cada equipo, incluyendo partidos jugados, goles convertidos, penales convertidos y promedio de goles por partido.

La aplicación fue desarrollada utilizando estructuras condicionales y repetitivas, funciones, listas, dataclass, validaciones de datos y modularización del código, siguiendo los contenidos abordados durante la asignatura.

  ## Funcionalidades principales

* Registrar equipos participantes.
* Mostrar la lista de equipos registrados.
* Registrar partidos indicando fecha, equipos participantes y resultado.
* Registrar penales convertidos únicamente cuando el partido finaliza empatado.
* Calcular automáticamente:

  * Partidos jugados.
  * Partidos ganados.
  * Partidos empatados.
  * Partidos perdidos.
  * Goles a favor.
  * Goles en contra.
  * Diferencia de gol.
  * Puntos obtenidos.
* Generar la tabla de posiciones ordenada automáticamente.
* Consultar estadísticas generales del torneo.
* Consultar estadísticas individuales de todos los equipos registrados.

  ## Reglas del sistema

* Se pueden registrar como máximo 16 equipos.
* No se permite registrar equipos con nombres repetidos.
* Los equipos registrados no pueden eliminarse.
* Un partido registrado no puede modificarse posteriormente.
* Un mismo enfrentamiento puede repetirse únicamente si corresponde a una fecha distinta.
* Los penales convertidos constituyen una estadística adicional y no modifican los puntos ni la tabla de posiciones.
* La tabla de posiciones se ordena según:

  1. Puntos obtenidos.
  2. Diferencia de gol.
  3. Goles a favor.


# Instrucciones de ejecución
   *Tener instalado Python 3.11 o superior
   *No es necesario instalar librerias adicionales 
     *Abrir una terminar o consola
     *Acceder a la carpeta donde se encuentra el sistemas
     *Ejecutar el programa con el siguiente comando: python main.py
