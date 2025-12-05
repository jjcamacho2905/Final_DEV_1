from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime, Enum as SQLEnum, func
from sqlalchemy.orm import relationship
from database import Base
from enum import Enum



class Jugador(Base):
    """Modelo de Jugador"""
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, index=True)
    edad = Column(Integer, nullable=False)
    posicion = Column(SQLEnum(Position), nullable=False)
    numero = Column(Integer, nullable=False, unique=True)  # Número de camiseta único
    estado = Column(SQLEnum(States), default=States.ACTIVO)
    foto_path = Column(String, nullable=True)
    fecha_registro = Column(DateTime, server_default=func.now())
    activo = Column(Boolean, default=True)

    pass


class Estadistica():
    pass


class Partido():
    pass

 # Estadísticas del jugador en ese partido específico
    goles_partido = Column(Integer, default=0)
    asistencias_partido = Column(Integer, default=0)
    minutos_jugados = Column(Integer, default=0)
    tarjeta_amarilla = Column(Boolean, default=False)
    tarjeta_roja = Column(Boolean, default=False)
