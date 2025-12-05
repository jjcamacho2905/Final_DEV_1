from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from db import Base, engine, get_db
import crud

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def inicio(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})

# ---------------- JUGADORES ----------------

@app.get("/jugadores", response_class=HTMLResponse)
def listar_jugadores(request: Request, db: Session = Depends(get_db)):
    jugadores = crud.obtener_jugadores(db)
    return templates.TemplateResponse("jugadores_listar.html", {"request": request, "jugadores": jugadores})

@app.get("/jugadores/crear", response_class=HTMLResponse)
def crear_jugador_form(request: Request):
    return templates.TemplateResponse("jugadores_crear.html", {"request": request})

@app.post("/jugadores/crear")
def crear_jugador(nombre: str = Form(...), numero: int = Form(...), fecha_nacimiento: str = Form(...), estado: str = Form(...), db: Session = Depends(get_db)):
    crud.crear_jugador(db, nombre, numero, fecha_nacimiento, estado)
    return RedirectResponse("/jugadores", status_code=303)

@app.get("/jugadores/{jugador_id}", response_class=HTMLResponse)
def detalle_jugador(jugador_id: int, request: Request, db: Session = Depends(get_db)):
    jugador = crud.obtener_jugador(db, jugador_id)
    historial = crud.obtener_participaciones_por_jugador(db, jugador_id)
    return templates.TemplateResponse("jugadores_detalle.html", {"request": request, "jugador": jugador, "historial": historial})

# ---------------- PARTIDOS ----------------

@app.get("/partidos", response_class=HTMLResponse)
def listar_partidos(request: Request, db: Session = Depends(get_db)):
    partidos = crud.obtener_partidos(db)
    return templates.TemplateResponse("partidos_listar.html", {"request": request, "partidos": partidos})

@app.get("/partidos/crear", response_class=HTMLResponse)
def crear_partido_form(request: Request):
    return templates.TemplateResponse("partidos_crear.html", {"request": request})

@app.post("/partidos/crear")
def crear_partido(rival: str = Form(...), fecha: str = Form(...), goles_propios: int = Form(...), goles_rival: int = Form(...), condicion: str = Form(...), db: Session = Depends(get_db)):
    crud.crear_partido(db, rival, fecha, goles_propios, goles_rival, condicion)
    return RedirectResponse("/partidos", status_code=303)
