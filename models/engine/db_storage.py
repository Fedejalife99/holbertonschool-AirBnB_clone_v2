#!/usr/bin/python3
"""New engine"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import Base
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """initialize the engine"""
        user = os.environ.get("HBNB_MYSQL_USER")
        passwd = os.environ.get("HBNB_MYSQL_PWD")
        datab = os.environ.get("HBNB_MYSQL_DB")
        host = os.environ.get("HBNB_MYSQL_HOST")
        env = os.environ.get("HBNB_ENV")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, datab),
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects of a class"""
        new_dict = {}

        if cls is not None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        for cls in classes:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f"{obj.__class__.__name__}.{obj.id}"
                new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload objects from the database"""
        Base.metadata.create_all(self.__engine)
        session_make = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_make)
        self.__session = Session()

    def close(self):
        """method on the private session attribute (self.__session)"""
        self.__session.close()
