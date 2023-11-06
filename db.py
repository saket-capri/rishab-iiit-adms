from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config
import sqlalchemy
# SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:passw@localhost:3306/attendance"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:passw@localhost:3306/attendance?charset=utf8mb4"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.orm.declarative_base()

def get_db():
    """
    Function to generate db session
    :return: Session
    """
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()