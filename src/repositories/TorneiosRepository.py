from src.model.Torneios import Torneios
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from src.model.Base import db

def add_torneio(id: int, nome: str,vencedor_id: None, local: str, ) -> Torneios:
    """
    Insert a Partida in the database.
    """
    torneio = Torneios(
        id=id,
        nome=nome,
        vencedor_id=vencedor_id,
        local=local
    )

    # INSERT
    db.session.add(torneio)
    db.session.commit()

    return torneio

def get_torneios() -> list[Torneios]:
    """
    Get all Partidas stored in the database.

    Returns:
        partidas (list[Partidas]) -- contains all partidas registered.
    """
    torneios = db.session.query(Torneios).all()
    return torneios

def get_torneio(id: int) -> Torneios:
    """
    Get partida by id stored in the database.

    Returns:
        partida (Partidas) -- contains one partida registered.
    """
    torneio = db.session.query(Torneios).get(id)
    return torneio

def update_torneio(id: int, nome=None, vencedor_id=None, local=None) -> Torneios:
    """
    Update a Partida in the database.
    """
    torneio = db.session.query(Torneios).get(id)

    if nome is None:
        nome = torneio.nome
    else:
        torneio.nome = nome

    if vencedor_id is None:
        vencedor_id = torneio.vencedor_id
    else:
        torneio.vencedor_id = vencedor_id

    if local is None:
        local = torneio.local
    else:
        torneio.local = local

        db.session.commit()

    return torneio

def delete_torneio(id: int):
    """
    Delete partida by id stored in the database.
    """
    torneio = db.session.query(Torneios).get(id)
    if torneio:
        db.session.delete(torneio)
        db.session.commit()
