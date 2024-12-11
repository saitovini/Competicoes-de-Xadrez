from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base

class Jogadores(Base):
    __tablename__ = "jogadores"

    # Columns
    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String(100), nullable=False)
    idade = Column("idade", Integer, nullable=False)

    categoria_fk = ForeignKey("categorias.id", ondelete="SET NULL")
    categoria_id = Column("categoria_id", categoria_fk, nullable=True)


    # Relationships
    categorias = relationship("Categorias", back_populates="jogadores")
    torneios = relationship("Torneios", back_populates="jogadores")
    partidas_jogador1 = relationship("Partidas", foreign_keys="[Partidas.jogador1_id]", back_populates="jogador1")
    partidas_jogador2 = relationship("Partidas", foreign_keys="[Partidas.jogador2_id]", back_populates="jogador2")
    partidas_vencedor = relationship("Partidas", foreign_keys="[Partidas.vencedor_id]", back_populates="vencedor")
