#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        @property
        def cities(self):
            """  returns the list of City instances with state_id equals
            to the current State.id """
            dict_city = storage.all(City)
            store = []
            for key, value in dict_city.items():
                if value.state_id == self.id:
                    store.append(value)
            return store
