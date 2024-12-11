from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base

class Categorias(Base):
    __tablename__ = "categorias"

    # Columns
    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String(5), nullable=False)
    descricao = Column("descricao", String(255), nullable=True)

    # Relationships
    jogadores = relationship("Jogadores", back_populates="categorias") 