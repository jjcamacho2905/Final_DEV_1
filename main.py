from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas, crud
from database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="sigmotoa FC - Sistema de Gestión",
    description="API para gestionar jugadores, estadísticas y partidos",
    version="1.0.0"
)



@app.get("/", tags=["Inicio"])
async def root():
    """Endpoint raíz"""
    return {
        "message": "sigmotoa FC - Sistema de Gestión de Fútbol",
        "version": "1.0.0",
        "endpoints": {
            "jugadores": "/jugadores",
            "estadisticas": "/estadisticas",
            "partidos": "/partidos",
            "docs": "/docs"
        }
    }


@app.get("/hello/{name}", tags=["Inicio"])
async def say_hello(name: str):
    """Saludo personalizado"""
    return {"message": f"Bienvenido a sigmotoa FC, {name}!"}


@app.post("/jugadores", response_model=schemas.Jugador, tags=["Jugadores"])
def crear_jugador_endpoint(jugador: schemas.JugadorCrear, db: Session = Depends(get_db)):
    """Crear un nuevo jugador"""
    return crud.crear_jugador(db, jugador)


@app.get("/jugadores", response_model=List[schemas.Jugador], tags=["Jugadores"])
def listar_jugadores(
    activos_solo: bool = True,
    db: Session = Depends(get_db)
):
    """Listar todos los jugadores"""
    return crud.obtener_jugadores(db, activos_solo)


@app.get("/jugadores/{jugador_id}", response_model=schemas.Jugador, tags=["Jugadores"])
def obtener_jugador(jugador_id: int, db: Session = Depends(get_db)):
    """Obtener un jugador por ID"""
    return crud.obtener_jugador_por_id(db, jugador_id)


@app.get("/jugadores/posicion/{posicion}", response_model=List[schemas.Jugador], tags=["Jugadores"])
def listar_por_posicion(posicion: models.Position, db: Session = Depends(get_db)):
    """Listar jugadores por posición"""
    return crud.obtener_jugadores_por_posicion(db, posicion)


@app.get("/jugadores/estado/{estado}", response_model=List[schemas.Jugador], tags=["Jugadores"])
def listar_por_estado(estado: models.States, db: Session = Depends(get_db)):
    """Listar jugadores por estado"""
    return crud.obtener_jugadores_por_estado(db, estado)


@app.patch("/jugadores/{jugador_id}", response_model=schemas.Jugador, tags=["Jugadores"])
def actualizar_jugador_endpoint(
    jugador_id: int,
    datos: schemas.JugadorActualizar,
    db: Session = Depends(get_db)
):
    """Actualizar información de un jugador"""
    return crud.actualizar_jugador(db, jugador_id, datos)


@app.patch("/jugadores/{jugador_id}/estado", tags=["Jugadores"])
def cambiar_estado(
    jugador_id: int,
    estado: models.States,
    db: Session = Depends(get_db)
):
    """Cambiar el estado de un jugador"""
    jugador = crud.cambiar_estado_jugador(db, jugador_id, estado)
    return {
        "mensaje": f"Estado actualizado a {estado.value}",
        "jugador": jugador
    }


@app.delete("/jugadores/{jugador_id}", tags=["Jugadores"])
def inactivar_jugador_endpoint(jugador_id: int, db: Session = Depends(get_db)):
    """Inactivar un jugador"""
    jugador = crud.inactivar_jugador(db, jugador_id)
    return {"mensaje": f"Jugador {jugador.nombre} inactivado"}

