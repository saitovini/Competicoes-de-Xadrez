from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base

class Torneios(Base):
    __tablename__ = "torneios"

    # Columns
    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String(100), nullable=False)
    vencedor_fk = ForeignKey("jogadores.id", ondelete="SET NULL")
    vencedor_id = Column("vencedor_id", vencedor_fk, nullable=True)
    local = Column("local", String(100), nullable=False)

    # Relationships
    jogadores = relationship("Jogadores", back_populates="torneios")
    partidas = relationship("Partidas", back_populates="torneios")
