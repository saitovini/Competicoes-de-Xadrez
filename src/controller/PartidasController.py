from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.PartidasService import deletePartida, updatePartida, addPartida, getPartida, getPartidas

class PartidaResponseSchema(Schema):
    id = fields.Int()
    torneio_id = fields.Int()
    jogador1_id = fields.Int()
    jogador2_id = fields.Int()
    data_partida = fields.Date()
    juiz_id = fields.Int()
    tipo = fields.Str()
    resultado = fields.Str()
    vencedor_id = fields.Int()

class PartidaRequestSchema(Schema):
    id = fields.Int()
    torneio_id = fields.Int()
    jogador1_id = fields.Int()
    jogador2_id = fields.Int()
    data_partida = fields.Date()
    juiz_id = fields.Int()
    tipo = fields.Str()
    resultado = fields.Str()
    vencedor_id = fields.Int()

class PartidaItem(MethodResource, Resource):
    @marshal_with(PartidaResponseSchema)
    def get(self, partida_id):
        try:
            partida = getPartida(partida_id)
            if not partida:
                abort(404, message="Partida não encontrada")
            return partida, 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    def delete(self, partida_id):
        try:
            deletePartida(partida_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Partida não encontrada")
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno do servidor")

    @use_kwargs(PartidaRequestSchema, location="form")
    @marshal_with(PartidaResponseSchema)
    def put(self, partida_id, **kwargs):
        try:
            partida = updatePartida(**kwargs, id=partida_id)
            return partida, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno do servidor")


class PartidaList(MethodResource, Resource):
    @marshal_with(PartidaResponseSchema(many=True))
    def get(self):
        try:
            return getPartidas(), 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    @use_kwargs(PartidaRequestSchema, location="form")
    @marshal_with(PartidaResponseSchema)
    def post(self, **kwargs):
        try:
            partida = addPartida(**kwargs)
            return partida, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
