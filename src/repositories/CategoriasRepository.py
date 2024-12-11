from src.model.Categorias import Categorias
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from src.model.Base import db

def add_categoria(id: int, nome: str, descricao: str) -> Categorias:
    """
    Insert a Categoria in the database.
    """
    categoria = Categorias(id=id, nome=nome, descricao=descricao)

    # INSERT
    db.session.add(categoria)
    db.session.commit()

    return categoria

def get_categorias() -> list[Categorias]:
    """
    Get all Categorias stored in the database.

    Returns:
        categorias (list[Categorias]) -- contains all categorias registered.
    """
    categorias = db.session.query(Categorias).all()
    return categorias

def get_categoria(id: int) -> Categorias:
    """
    Get categoria by id stored in the database.

    Returns:
        categoria (Categorias) -- contains one categoria registered.
    """
    categoria = db.session.query(Categorias).get(id)
    return categoria

def update_categoria(id: int, nome=None, descricao=None) -> Categorias:
    """
    Update a Categoria in the database.
    """
    categoria = db.session.query(Categorias).get(id)

    if nome is None:
        nome = categoria.nome
    else:
        categoria.nome = nome

    if descricao is None:
        descricao = categoria.descricao
    else:
        categoria.descricao = descricao


    db.session.commit()

    return categoria

def delete_categoria(id: int):
    """
    Delete categoria by id stored in the database.
    """
    categoria = db.session.query(Categorias).get(id)
    db.session.delete(categoria)
    db.session.commit()
