#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, relationship
from models.base_model import Base, BaseModel
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == 'db':
      cities = relationship("state", back_populates="states", cascade="all, delete-  orphan")
    else:
      @property
      def cities(self):
        from models import storage
        from models import City
        cities = storage.all(City)
        return [City for city in cities if City.states_id == State.id]