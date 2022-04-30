from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Reportefinal(Base):
    """ORM Mapped Class for reportefinal table"""

    __tablename__ = "reportefinal"
    franja = Column(String(50), nullable=False, primary_key=True)
    dosis1 = Column(Integer, nullable=False)
    dosis2 = Column(Integer, nullable=False)
    dosis3 = Column(Integer, nullable=False)
    dosis4 = Column(Integer, nullable=False)
    dosis5 = Column(Integer, nullable=False)
    esp_dosis1 = Column(Integer, nullable=False)
    esp_dosis2 = Column(Integer, nullable=False)
    esp_dosis3 = Column(Integer, nullable=False)
    esp_dosis4 = Column(Integer, nullable=False)
    esp_dosis5 = Column(Integer, nullable=False)
    agen_dosis2 = Column(Integer, nullable=False)
    agen_dosis1 = Column(Integer, nullable=False)
    agen_dosis3 = Column(Integer, nullable=False)
    agen_dosis4 = Column(Integer, nullable=False)
    agen_dosis5 = Column(Integer, nullable=False)
    timestamp = Column(Date, nullable=False, primary_key=True)
