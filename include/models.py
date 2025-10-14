from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .db import Base
from datetime import datetime, timezone, timedelta

def get_saopaulo_time():
    return datetime.now(timezone(timedelta(hours=-3)))

class Cotacao(Base):
    __tablename__ = 'cotacao'
    id = Column(Integer, primary_key=True, index=True)
    criptomoeda = Column(String(50), nullable = False)
    moeda = Column(String(20))
    valor = Column(Float)
    created_at = Column(
        DateTime(timezone=True), 
        default=get_saopaulo_time
    )