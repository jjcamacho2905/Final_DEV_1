from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session, select
from starlette.status import HTTP_303_SEE_OTHER
from db import get_session
from models import Estadistica

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def listar_estadisticas(request: Request, session: Session = Depends(get_session)):
    carros = session.exec(select(Estadistica)).all()

    return request.app.state.templates.TemplateResponse(
        "estadisticas_list.html",
        {"request": request, "carros": carros}
    )
