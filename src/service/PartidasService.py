from sqlalchemy import Date
from src.model.Partidas import Partidas
from src.repositories.PartidasRepository import (
    delete_partida,
    update_partida,
    get_partida,
    add_partida,
    get_partidas
)

def addPartida(id: int,  jogador1_id: int, jogador2_id: int, data_partida: Date, juiz_id: int, tipo=None, resultado=None, vencedor_id=None, torneio_id= None) -> Partidas:
    """
    Add a Partida to the database.
    """
    if id is None or id == '' or data_partida is None or jogador1_id is None or jogador2_id is None:
        raise Exception("ID, data da partida, jogador1_id, e jogador2_id são obrigatórios para adicionar uma partida.")

    return add_partida(id, torneio_id, jogador1_id, jogador2_id, data_partida, juiz_id, tipo, resultado, vencedor_id)

def getPartidas() -> list[Partidas]:
    """
    Get all Partidas stored in the database.

    Returns:
        partidas (list[Partidas]) -- contains all partidas registered.
    """
    return get_partidas()

def getPartida(id: int) -> Partidas:
    """
    Get partida by id stored in the database.

    Returns:
        partida (Partidas) -- contains one partida registered.
    """
    return get_partida(id)

def updatePartida(id: int, torneio_id=None, jogador1_id=None, jogador2_id=None, data_partida=None, juiz_id=None, tipo=None, resultado=None, vencedor_id=None) -> Partidas:
    """
    Update a Partida in the database.
    """
    return update_partida(
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

def deletePartida(id: int):
    """
    Delete partida by id stored in the database.
    """
    delete_partida(id)
