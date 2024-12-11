from src.model.Torneios import Torneios
from src.repositories.TorneiosRepository import (
    delete_torneio,
    update_torneio,
    get_torneio,
    add_torneio,
    get_torneios
)

def addTorneio(id: int, nome: str, local: str,vencedor_id=None ) -> Torneios:
    """
    Add a Torneio to the database.
    """
    if (id is None or id == '') or (nome is None or nome == '') or (local is None or local == ''):
        raise Exception("ID, nome e local são obrigatórios para adicionar um torneio.")

    return add_torneio(id, nome, vencedor_id, local)

def getTorneios() -> list[Torneios]:
    """
    Get all Torneios stored in the database.

    Returns:
        torneios (list[Torneios]) -- contains all torneios registered.
    """
    return get_torneios()

def getTorneio(id: int) -> Torneios:
    """
    Get torneio by id stored in the database.

    Returns:
        torneio (Torneios) -- contains one torneio registered.
    """
    return get_torneio(id)

def updateTorneio(id: int, nome=None,  local=None,vencedor_id= None) -> Torneios:
    """
    Update a Torneio in the database.
    """
    return update_torneio(id=id, nome=nome, vencedor_id=vencedor_id, local=local)

def deleteTorneio(id: int):
    """
    Delete torneio by id stored in the database.
    """
    delete_torneio(id)
