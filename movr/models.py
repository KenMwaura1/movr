"""
Aligns sqlalchemy's schema for the "vehicles" table with the database.
"""

from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        PrimaryKeyConstraint, String)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func

Base = declarative_base()


class Vehicle(Base):
    """
    DeclarativeMeta class for the vehicles table.

    Arguments:
        Base {DeclarativeMeta} -- Base class for model to inherit.
    """
    __tablename__ = 'vehicles'
    # FOR THE LAB, UPDATE THIS CLASS FOR THE NEW SCHEMA
    # THE CLASS DOESN'T MATCH THE CURRENT SCHEMA
    id = Column(UUID)
    # last_longitude = Column(Float)
    # last_latitude = Column(Float)
    # last_checkin = Column(DateTime, default=func.now)
    in_use = Column(Boolean)
    vehicle_type = Column(String)
    battery = Column(Integer)
    PrimaryKeyConstraint(id)

    def __repr__(self):
        return "<Vehicle(id='{0}', vehicle_type='{1}')>".format(
            self.id, self.vehicle_type)


class LocationHistory(Base):
    """
    Table object to store a vehicle's location_history.

    Arguments:
        Base {DeclarativeMeta} -- Base class for declarative SQLAlchemy class
                that produces appropriate `sqlalchemy.schema.Table` objects.
    """
    __tablename__ = 'location_history'
    id = Column(UUID, primary_key=True)
    vehicle_id = Column(UUID, ForeignKey('vehicles.id'))
    longitude = Column(Float)
    latitude = Column(Float)
    ts = Column(DateTime, default=func.now)
    PrimaryKeyConstraint(id)

    def __repr__(self):
        return (("<Vehicle(id='{1}', vehicle_id='{2}', ts='{3}', "
                 "longitude='{4}', latitude='{5}')>"
                 ).format(self.id, self.vehicle_id, self.ts, self.longitude,
                          self.latitude))
