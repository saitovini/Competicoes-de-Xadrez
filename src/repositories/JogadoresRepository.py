from src.model.Jogadores import Jogadores
from src.model.Base import db
from sqlalchemy.exc import IntegrityError, NoResultFound

def add_jogador(id: int, nome:str, idade:int, categoria_id=None) -> Jogadores:
    """
    Insert a Partida in the database.
    """
    jogador = Jogadores(
        id=id,
        nome=nome,
        idade = idade,
        categoria_id= categoria_id,
    )



    # INSERT
    db.session.add(jogador)
    db.session.commit()

    return jogador

def get_jogadores() -> list[Jogadores]:
    """
    Get all Partidas stored in the database.

    Returns:
        partidas (list[Partidas]) -- contains all partidas registered.
    """
    jogadores = db.session.query(Jogadores).all()
    return jogadores

def get_jogador(id: int) -> Jogadores:
    """
    Get partida by id stored in the database.

    Returns:
        partida (Partidas) -- contains one partida registered.
    """
    jogador = db.session.query(Jogadores).get(id)
    return jogador

def update_jogador(id: int,  nome= None, idade= None, categoria_id= None) -> Jogadores:
    """
    Update a Jogador in the database.
    O que está acontecendo é: nome, por exemplo, está sendo passado como None, com isso cai no if e ele se fica igual
        ao nome que está armazenado no banco, caso contrário, caso seja passado um valor, ele é igual ao novo valor
    """
    jogador = db.session.query(Jogadores).get(id)

    if nome is None:
        nome = jogador.nome
    else:
        jogador.nome = nome
    if idade is None:
        idade = jogador.idade
    else:
        jogador.idade = idade

    if categoria_id is None:
        categoria_id = jogador.categoria_id
    else:
        jogador.categoria_id = categoria_id


    db.session.commit()
    return jogador


def delete_jogador(id: int):
    """
    Delete partida by id stored in the database.
    """
    jogador = db.session.query(Jogadores).get(id)
    db.session.delete(jogador)
    db.session.commit()