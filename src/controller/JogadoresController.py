import re
from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.JogadoresService import deleteJogador, updateJogador, addJogador, getJogador, getJogadores

class JogadorResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    idade = fields.Int()
    categoria_id = fields.Int()

class JogadorRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    idade = fields.Int()
    categoria_id = fields.Int()

    @validates("nome")
    def validate_name(self, value):
        if not re.match(r"^[a-zA-Z0-9_\s]+$", value):
            raise ValidationError("Nome deve conter apenas caracteres alfanuméricos e underscores.")

class JogadorItem(MethodResource, Resource):
    @marshal_with(JogadorResponseSchema)
    def get(self, jogador_id):
        try:
            jogador = getJogador(jogador_id)
            if not jogador:
                abort(404, message="Jogador não encontrado")
            return jogador, 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    def delete(self, jogador_id):
        try:
            deleteJogador(jogador_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Jogador não encontrado")
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno do servidor")

    @use_kwargs(JogadorRequestSchema, location="form")
    @marshal_with(JogadorResponseSchema)
    def put(self, jogador_id, **kwargs):
        try:
            jogador = updateJogador( **kwargs, id=jogador_id)
            return jogador, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno do servidor")


class JogadorList(MethodResource, Resource):
    @marshal_with(JogadorResponseSchema(many=True))
    def get(self):
        try:
            return getJogadores(), 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    @use_kwargs(JogadorRequestSchema, location="form")
    @marshal_with(JogadorResponseSchema)
    def post(self, **kwargs):
        try:
            jogador = addJogador(**kwargs)
            return jogador, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
