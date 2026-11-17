#!/usr/bin/python3
"""Defines the City model mapped to the cities table."""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """A city of the USA stored in the cities table, linked to a state."""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
