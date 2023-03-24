#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'Cities'
    state_id = Column(String(60), nullable=False, foregin_key=True)
    name = Column(String(128), nullable=False)