from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class ExchangeRate(Base):
    __tablename__ = 'exchange_rates'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, nullable=False, unique=True)
    exchange_rate = Column(Float(precision=4), nullable=False)


engine = create_engine('sqlite:///exchange_rate.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
