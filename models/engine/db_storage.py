#!/usr/bin/python3
"""New engine"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
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

        self.__engine = create_engine('postgresql://HBNB_MYSQL_USER:HBNB_MYSQL_PWD@HBNB_MYSQL_HOST/HBNB_MYSQL_DB',pool_pre_ping=True)
        #arreglar esto
        
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        
        self.__session = sessionmaker(self.__engine)
    def all(self, cls=None):
        """"""
        if cls is not None:
            query = self.__session.query(cls).all()
            
        else:
            query = self.__session.query.all()
            

        