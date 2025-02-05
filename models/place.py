#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_type == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
            'Review',
            cascade="all,delete",
            backref="place"
        )
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            back_populates="place_amenities",
            viewonly=False,
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Reviews getter"""
            from models import storage
            reviews_list = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id in self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            from models.__init__ import storage
            from models.amenity import Amenity

            obj_list = []
            strg = storage.all(Amenity)
            for value in strg:
                if self.id == value.id:
                    obj_list.append(value)
            return obj_list

        @amenities.setter
        def amenities(self, obj):
            from models.__init__ import storage
            from models.amenity import Amenity

            if isinstance(obj, storage.all(Amenity)):
                self.amenity_ids.append(obj.id)
