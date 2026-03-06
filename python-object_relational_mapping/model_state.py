#!/usr/bin/python3
"""Model State class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # Common base for all models


class State(Base):
    """State class that links to table states"""
    __tablename__ = 'states'  # name of the table
    # columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
