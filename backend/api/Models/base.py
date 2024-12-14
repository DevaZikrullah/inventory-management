from api import db,fields,SQLAlchemy
from sqlalchemy import Column, DateTime
from sqlalchemy.event import listens_for
from datetime import datetime

class Base(db.Model):
    __abstract__ = True
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)