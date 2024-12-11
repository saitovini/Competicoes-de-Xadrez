from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.JuizesService import deleteJuiz, updateJuiz, addJuiz, getJuiz, getJuizes

class JuizResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()


class JuizRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()

class JuizItem(MethodResource, Resource):
    @marshal_with(JuizResponseSchema)
    def get(self, juiz_id):
        try:
            juiz = getJuiz(juiz_id)
            if not juiz:
                abort(404, message="Juiz não encontrado")
            return juiz, 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    def delete(self, juiz_id):
        try:
            deleteJuiz(juiz_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Juiz não encontrado")
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno do servidor")

    @use_kwargs(JuizRequestSchema, location="form")
    @marshal_with(JuizResponseSchema)
    def put(self, juiz_id, **kwargs):
        try:
            juiz = updateJuiz(**kwargs, id=juiz_id)
            return juiz, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno do servidor")


class JuizList(MethodResource, Resource):
    @marshal_with(JuizResponseSchema(many=True))
    def get(self):
        try:
            return getJuizes(), 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    @use_kwargs(JuizRequestSchema, location="form")
    @marshal_with(JuizResponseSchema)
    def post(self, **kwargs):
        try:
            juiz = addJuiz(**kwargs)
            return juiz, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
