from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base

class Juizes(Base):
    __tablename__ = "juizes"

    # Columns
    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String(100), nullable=False)

    # Relationships
    partidas = relationship("Partidas", back_populates="juizes")