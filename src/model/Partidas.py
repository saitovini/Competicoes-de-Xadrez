from sqlalchemy import Column, Date, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from .Base import Base

class Partidas(Base):
    __tablename__ = 'partidas'

    # Columns
    id = Column("id", Integer, primary_key=True)
    torneio_fk = ForeignKey("torneios.id", ondelete="SET NULL")
    torneio_id = Column("torneio_id", torneio_fk, nullable=True)

    jogador1_fk = ForeignKey("jogadores.id", ondelete="SET NULL")
    jogador1_id = Column("jogador1_id", jogador1_fk, nullable=False)

    jogador2_fk = ForeignKey("jogadores.id", ondelete="SET NULL")
    jogador2_id = Column("jogador2_id", jogador2_fk, nullable=False)

    data_partida = Column("data_partida", Date, nullable=False)
    juiz_fk = ForeignKey("juizes.id", ondelete="SET NULL")
    juiz_id = Column("juiz_id", juiz_fk, nullable=False)

    tipo = Column("tipo", String(50), nullable=True)
    resultado = Column("resultado", String(255), nullable=True)

    vencedor_fk = ForeignKey("jogadores.id", ondelete="SET NULL")
    vencedor_id = Column("vencedor_id", vencedor_fk, nullable=True)

    # Relationships
    torneios = relationship("Torneios", back_populates="partidas")
    juizes = relationship("Juizes", back_populates="partidas")
    jogador1 = relationship("Jogadores", foreign_keys=[jogador1_id], back_populates="partidas_jogador1")
    jogador2 = relationship("Jogadores", foreign_keys=[jogador2_id], back_populates="partidas_jogador2")
    vencedor = relationship("Jogadores", foreign_keys=[vencedor_id], back_populates="partidas_vencedor")

