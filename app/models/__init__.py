from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CalculationHistory(Base):
    __tablename__ = 'calculation_history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    operation = Column(String, nullable=False)
    operand1 = Column(Float, nullable=False)
    operand2 = Column(Float, nullable=False)
    result = Column(Float, nullable=False)
