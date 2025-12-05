from dataclasses import field
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date
from utils.positions import Position
from utils.states import States

class JugadorEstadisticasLink(SQLModel, table=True):
    jugador_dorsal: Optional[int] = Field(default=None, foreign_key="jugador.dorsal", primary_key=True) ##
    estadistica_id: Optional[int] = Field(default=None, foreign_key="estadistica.id", primary_key=True)

class JugadorPosicionLink(SQLModel, table=True):
    jugador_dorsal: Optional[int] = Field(default=None, foreign_key="jugador.dorsal", primary_key=True)
    posicion: Optional[int] = Field(default=None, foreign_key="position.", primary_key=True)

class JugadorBase(SQLModel):
    dorsal[int] = Field(default=None, primary_key=True)   ##
    nombre: Optional[str]=None
    altura: Optional[float]=None
    peso: Optional[float]=None
    año_nacimiento: Optional[date]=None
    pie_dominante: Optional[str]=None
    tiempo_cancha: Optional[int]=None
    goles: Optional[int]=None
    faltas: Optional[int]=None
    fecha_nacimiento: Optional[date]=None

    

class Jugador(JugadorBase, table=True):
    dorsal:Optional[str]=None
    nombre = Optional[str]=None
    active: bool = Field(default=True)
    estadisticas: List[Estadistica] = Relationship(back_populates="jugador", link_model=JugadorEstadisticasLink)
    posición: List[str]= Relationship(back_populates="")

class EstadisticaBase(SQLModel):
    goles: Optional[int]=None
    faltas: Optional[int]=None
    tiempo_de_juego:[int]=None


class Estadistica(EstadisticaBase, table=True):
    id: Optional[int]


class Partido():
    pass
