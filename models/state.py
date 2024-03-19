#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from models.city import City
from models import storage_type
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    if storage_type == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all,\
                              delete-orphan')

    else:
        name = ""

        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
