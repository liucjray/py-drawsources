from sqlalchemy import create_engine, Column, Integer, String, Float, PrimaryKeyConstraint, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import *

from database.connection import *

Base = declarative_base()


class IssueInfo(Base):
    __tablename__ = "issue_info2"
    id = Column(Integer, primary_key=True)
    resource = Column(String)
    type = Column(String)
    area = Column(String)
    issue = Column(String)
    code = Column(String)
    info = Column(String)
    draw_at = Column(DateTime)
    created_at = Column(DateTime)


engine = get_instance()
IssueInfo.__table__.create(bind=engine, checkfirst=True)
