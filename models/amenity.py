#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
