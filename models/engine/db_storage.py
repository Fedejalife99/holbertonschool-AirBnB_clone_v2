#!/usr/bin/python3
"""New engine"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scooped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    __engine = None
    __session = None

    def __init__ (self):
        """initialize the engine"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        datab = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine =  create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, datab), pool_pre_ping=True)
        
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        
        
      
    def all(self, cls=None):
        """"""
        new_dict = {}
        if cls is not None:
          query = self.__session.query(cls).all()
        else:
          query = self.__session.query.all()

        for values in query:
          new_dict[cls.id] = values

        return new_dict

    def new(self, obj):
      self.__session.add(obj)

    def save(self,obj):
      self.__session.save(obj)

    def delete(self, obj=None):
      self.__session.delete(obj)
      
    def reload(self):
      Base.metadata.create_all(self.__engine)
      self.__session = scooped_session(sessionmaker(self.__engine, expire_on_commit=False))