from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
import sqlalchemy
# from databases import Database
SQLALCHEMY_DATABASE_URL = "mysql+pymysql:///attendance?charset=utf8mb4"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.orm.declarative_base()

def get_db():
    """
    Function to generate db session
    :return: Session
    """
    # print(settings)
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()