#!/usr/bin/python3
"""State Class definition"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Table parameters creation"""
    __tablename__ = 'states'
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False
        )
    name = Column(
        String(128),
        nullable=False
        )
