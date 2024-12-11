from src.model.Categorias import Categorias
from src.repositories.CategoriasRepository import (
    delete_categoria,
    update_categoria,
    get_categoria,
    add_categoria,
    get_categorias
)

def addCategoria(id: int, nome: str, descricao: str) -> Categorias:
    if id is None or id == '' or nome is None or nome == '':
        raise Exception("ID e nome são obrigatórios para adicionar uma categoria.")

    return add_categoria(id, nome, descricao)

def getCategorias() -> list[Categorias]:
    return get_categorias()

def getCategoria(id: int) -> Categorias:
    return get_categoria(id)

def updateCategoria(id: int, nome: str, descricao= None):
    return update_categoria(id=id, nome=nome, descricao=descricao)

def deleteCategoria(id: int):
    delete_categoria(id)
