#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
import models
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_ref="state", cascade="all, delete-orphan")
    
    @property
    def cities(self):
        from models.city import City
        return [city for city in models.storage.all(City).values() if city.state_id == self.id]