import re
from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.CategoriasService import deleteCategoria, updateCategoria, addCategoria, getCategoria, getCategorias

class CategoriaResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    descricao = fields.Str()

class CategoriaRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    descricao = fields.Str()

    @validates("nome")
    def validate_name(self, value):
        if not re.match(pattern=r"^[a-zA-Z0-9_\s]+$", string=value):
            raise ValidationError(
                "Nome deve conter apenas caracteres alfanuméricos e underscores."
            )

class CategoriaItem(MethodResource, Resource):
    @marshal_with(CategoriaResponseSchema)
    def get(self, categoria_id):
        try:
            categoria = getCategoria(categoria_id)
            if not categoria:
                abort(404, message="Recurso não encontrado")
            return categoria, 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    def delete(self, categoria_id):
        try:
            deleteCategoria(categoria_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Recurso não encontrado")
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno do servidor")

    @use_kwargs(CategoriaRequestSchema, location=("form"))
    @marshal_with(CategoriaResponseSchema)
    def put(self, categoria_id, **kwargs):
        try:
            categoria = updateCategoria(**kwargs, id=categoria_id)
            return categoria, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno do servidor")


class CategoriaList(MethodResource, Resource):
    @marshal_with(CategoriaResponseSchema(many=True))
    def get(self):
        try:
            return getCategorias(), 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    @use_kwargs(CategoriaRequestSchema, location=("form"))
    @marshal_with(CategoriaResponseSchema)
    def post(self, **kwargs):
        try:
            categoria = addCategoria(**kwargs)
            return categoria, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
