from src.model.Juizes import Juizes
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from src.model.Base import db

def add_juiz(id: int, nome: str) -> Juizes:
    """
    Insert a Juiz in the database.
    """
    juiz = Juizes(
        id=id,
        nome=nome
    )

    db.session.add(juiz)
    db.session.commit()

    return juiz

def get_juizes() -> list[Juizes]:
    """
    Get all Juizes stored in the database.

    Returns:
        juizes (list[Juizes]) -- contains all juizes registered.
    """
    juizes = db.session.query(Juizes).all()
    return juizes

def get_juiz(id: int) -> Juizes:
    """
    Get juiz by id stored in the database.

    Returns:
        juiz (Juizes) -- contains one juiz registered.
    """
    juiz = db.session.query(Juizes).get(id)
    return juiz

def update_juiz(id: int, nome: str) -> Juizes:
    """
    Update a Juiz in the database.
    """
    juiz = db.session.query(Juizes).get(id)

    juiz.nome = nome
    db.session.commit()

    return juiz

def delete_juiz(id: int):
    """
    Delete juiz by id stored in the database.
    """
    juiz = db.session.query(Juizes).get(id)
    db.session.delete(juiz)
    db.session.commit()
