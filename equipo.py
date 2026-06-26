from dataclasses import dataclass

@dataclass
class Equipo:
    nombre: str
    pj: int = 0
    pg: int = 0
    pe: int = 0
    pp: int = 0

    gf: int = 0          # Goles a favor
    gc: int = 0          # Goles en contra
    dg: int = 0          # Diferencia de gol

    pts: int = 0

    penales_convertidos: int = 0