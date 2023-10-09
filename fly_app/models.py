from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime, CheckConstraint
from sqlalchemy.orm import relationship, sessionmaker, registry
from sqlalchemy.ext.declarative import declarative_base
from fly_app import Base, engine
from pydantic import BaseModel


Session = sessionmaker(bind=engine)
session = Session()

mapper_registry = registry()
mapper_registry.configure()

Base = declarative_base()




