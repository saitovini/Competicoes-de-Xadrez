from src.model.Jogadores import Jogadores
from src.repositories.JogadoresRepository import (
    delete_jogador,
    update_jogador,
    get_jogador,
    add_jogador,
    get_jogadores
)

def addJogador(id: int, nome: str, idade: int, categoria_id=None) -> Jogadores:
    """
    Add a Jogador to the database.
    """
    if id is None or id == '' or nome is None or nome == '' or idade is None:
        raise Exception("ID, nome e idade são obrigatórios para adicionar um jogador.")

    return add_jogador(id, nome, idade, categoria_id)

def getJogadores() -> list[Jogadores]:
    """
    Get all Jogadores stored in the database.

    Returns:
        jogadores (list[Jogadores]) -- contains all jogadores registered.
    """
    return get_jogadores()

def getJogador(id: int) -> Jogadores:
    """
    Get jogador by id stored in the database.

    Returns:
        jogador (Jogadores) -- contains one jogador registered.
    """
    return get_jogador(id)

def updateJogador(id: int,  nome= None, idade= None, categoria_id= None) -> Jogadores:
    """
    Update a Jogador in the database.
    """
    return update_jogador(id=id, nome=nome, idade=idade, categoria_id=categoria_id)

def deleteJogador(id: int):
    """
    Delete jogador by id stored in the database.
    """
    delete_jogador(id)
