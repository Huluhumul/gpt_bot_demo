
from sqlalchemy import create_engine
from sqlalchemy import (
    Column,
    Text,
    Integer,
    String,
    ForeignKey,
    Float,
    Boolean,
    Table,
    JSON,
    BigInteger,
    DateTime,
)
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import config

base = declarative_base()


class User(base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    username = Column(String(length=50))
    tg_id = Column(BigInteger, unique=True)
    phone = Column(String(length=17))


engine = create_engine(URL(**config.db_connect_data, query={}))
base.metadata.create_all(engine)

session_maker = sessionmaker(bind=engine)
scoped_session_maker = scoped_session(sessionmaker(bind=engine))
global_session = session_maker()
