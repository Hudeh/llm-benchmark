from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from db.base import Base

class LLM(Base):
    __tablename__ = 'llms'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    simulation_results = relationship("SimulationResult", back_populates="llm")
    rankings = relationship("Ranking", back_populates="llm")


class Metric(Base):
    __tablename__ = 'metrics'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    simulation_results = relationship("SimulationResult", back_populates="metric")
    rankings = relationship("Ranking", back_populates="metric")


class SimulationResult(Base):
    __tablename__ = 'simulation_results'
    id = Column(Integer, primary_key=True, index=True)
    llm_id = Column(Integer, ForeignKey('llms.id'))
    metric_id = Column(Integer, ForeignKey('metrics.id'))
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    llm = relationship("LLM", back_populates="simulation_results")
    metric = relationship("Metric", back_populates="simulation_results")


class Ranking(Base):
    __tablename__ = 'rankings'
    id = Column(Integer, primary_key=True, index=True)
    metric_id = Column(Integer, ForeignKey('metrics.id'))
    llm_id = Column(Integer, ForeignKey('llms.id'))
    mean_value = Column(Float, nullable=False)
    rank = Column(Integer, nullable=False)

    metric = relationship("Metric", back_populates="rankings")
    llm = relationship("LLM", back_populates="rankings")

    __table_args__ = (
        UniqueConstraint('metric_id', 'llm_id', name='_metric_llm_uc'),
    )
