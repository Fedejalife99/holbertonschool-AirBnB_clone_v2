#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", back_ref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City
            cities = storage.all(City)
            return [city for city in cities.values() if city.state_id == self.id]