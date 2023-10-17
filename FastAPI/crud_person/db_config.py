from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'postgresql://username:password@host_adreess:port_number/db_name'

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class DefaultTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), primary_key=True)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)
