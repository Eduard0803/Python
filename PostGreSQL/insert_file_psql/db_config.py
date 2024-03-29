from sqlalchemy import Column, Integer, LargeBinary, MetaData, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://username:password@host_adreess:port_number/db_name"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class DefaultTable(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(100))
    file_content = Column(LargeBinary)


Base.metadata.create_all(bind=engine)
