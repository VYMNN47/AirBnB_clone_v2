#!/usr/bin/python3
"""contains DBStorage class"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

classes = {"State": State, "City": City, "User": User, "Place": Place,
           "Review": Review, "Amenity": Amenity}


class DBStorage:
    """DB Storage engine for mysql"""
    __engine = None
    __session = None

    def __init__(self):
        """contains env variables and engine initialization"""
        user = getenv("HBNB_MYSQL_USER")
        pswrd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(user,
                                                      pswrd,
                                                      host,
                                                      db)

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        returns a dictionary containing objects
        """

        dct = {}
        if cls is None:
            for c in classes.values():
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dct[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dct[key] = obj
        return dct

        return obj_dict

    def new(self, obj):
        """
        add the objects to the  current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """

        """
        Base.metadata.create_all(self.__engine)
        fsession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(fsession)
        self.__session = Session()

    def close(self):
        self.__session.close()
