from src.model.Partidas import Partidas
import sqlalchemy
from sqlalchemy import Date
from flask_sqlalchemy import SQLAlchemy
from src.model.Base import db

def add_partida(id: int, torneio_id: None, jogador1_id: str, jogador2_id: str, data_partida: Date, juiz_id: int, tipo: None, resultado:None, vencedor_id:None) -> Partidas:
    """
    Insert a Partida in the database.
    """
    partida = Partidas(
        id=id,
        torneio_id=torneio_id,
        jogador1_id=jogador1_id,
        jogador2_id=jogador2_id,
        data_partida=data_partida,
        juiz_id=juiz_id,
        tipo=tipo,
        resultado=resultado,
        vencedor_id=vencedor_id
    )

    # INSERT
    db.session.add(partida)
    db.session.commit()

    return partida

def get_partidas() -> list[Partidas]:
    """
    Get all Partidas stored in the database.

    Returns:
        partidas (list[Partidas]) -- contains all partidas registered.
    """
    partidas = db.session.query(Partidas).all()
    return partidas

def get_partida(id: int) -> Partidas:
    """
    Get partida by id stored in the database.

    Returns:
        partida (Partidas) -- contains one partida registered.
    """
    partida = db.session.query(Partidas).get(id)
    return partida

def update_partida(id: int, torneio_id=None, jogador1_id=None, jogador2_id=None, data_partida=None, juiz_id=None, tipo=None, resultado=None, vencedor_id=None) -> Partidas:
    """
    Update a Partida in the database.
    """
    partida = db.session.query(Partidas).get(id)

    if torneio_id is None:
        torneio_id = partida.torneio_id
    else:
        partida.torneio_id = torneio_id

    if jogador1_id is None:
        jogador1_id = partida.jogador1_id
    else:
        partida.jogador1_id = jogador1_id

    if jogador2_id is None:
        jogador2_id = partida.jogador2_id
    else:
        partida.jogador2_id = jogador2_id

    if data_partida is None:
        data_partida = partida.data_partida
    else:
        partida.data_partida = data_partida

    if juiz_id is None:
        juiz_id = partida.juiz_id
    else:
        partida.juiz_id = juiz_id

    if tipo is None:
        tipo = partida.tipo
    else:
        partida.tipo = tipo

    if resultado is None:
        resultado = partida.resultado
    else:
        partida.resultado = resultado

    if vencedor_id is None:
        vencedor_id = partida.vencedor_id
    else:
        partida.vencedor_id = vencedor_id

    db.session.commit()

    return partida

def delete_partida(id: int):
    """
    Delete partida by id stored in the database.
    """
    partida = db.session.query(Partidas).get(id)
    db.session.delete(partida)
    db.session.commit()
