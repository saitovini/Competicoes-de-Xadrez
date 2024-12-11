from flask import request
from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.TorneiosService import deleteTorneio, updateTorneio, addTorneio, getTorneio, getTorneios

class TorneioResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    vencedor_id = fields.Int()
    local = fields.Str()

class TorneioRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    vencedor_id = fields.Int()
    local = fields.Str()

class TorneioItem(MethodResource, Resource):
    @marshal_with(TorneioResponseSchema)
    def get(self, torneio_id):
        try:
            torneio = getTorneio(torneio_id)
            if not torneio:
                abort(404, message="Torneio não encontrado")
            return torneio, 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    def delete(self, torneio_id):
        try:
            deleteTorneio(torneio_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Torneio não encontrado")
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno do servidor")

    @use_kwargs(TorneioRequestSchema, location="form")
    @marshal_with(TorneioResponseSchema)
    def put(self, torneio_id, **kwargs):
        try:
            torneio = updateTorneio(**kwargs, id=torneio_id)
            return torneio, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno do servidor")


class TorneioList(MethodResource, Resource):
    @marshal_with(TorneioResponseSchema(many=True))
    def get(self):
        try:
            return getTorneios(), 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    @use_kwargs(TorneioRequestSchema, location="form")
    @marshal_with(TorneioResponseSchema)
    def post(self, **kwargs):
        try:
            torneio = addTorneio(**kwargs)
            return torneio, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
