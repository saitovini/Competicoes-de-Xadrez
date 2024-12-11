from src.model.Juizes import Juizes
from src.repositories.JuizesRepository import (
    delete_juiz,
    update_juiz,
    get_juiz,
    add_juiz,
    get_juizes
)

def addJuiz(id: int, nome: str) -> Juizes:
    """
    Add a Juiz to the database.
    """
    if (id is None or id == '' or nome is None or nome == ''):
        raise Exception("ID e nome são obrigatórios para adicionar um juiz.")

    return add_juiz(id, nome)

def getJuizes() -> list[Juizes]:
    """
    Get all Juizes stored in the database.

    Returns:
        juizes (list[Juizes]) -- contains all juizes registered.
    """
    return get_juizes()

def getJuiz(id: int) -> Juizes:
    """
    Get juiz by id stored in the database.

    Returns:
        juiz (Juizes) -- contains one juiz registered.
    """
    return get_juiz(id)

def updateJuiz(id: int, nome: str) -> Juizes:
    """
    Update a Juiz in the database.
    """
    return update_juiz(id=id, nome=nome)

def deleteJuiz(id: int):
    """
    Delete juiz by id stored in the database.
    """
    delete_juiz(id)
