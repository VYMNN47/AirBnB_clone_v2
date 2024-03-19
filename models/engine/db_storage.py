#!/usr/bin/python3

from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
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

        objs = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                objs = self.__session.query(cls).all()
        else:
            for sclass in Base.__subclasses__():
                objs.extend(self.__session.query(sclass).all())

        objs_dict = {}

        for obj in objs:
            key = "{}.{}".format(class_.__name__, obj.id)
            objs_dict[key] = obj

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
