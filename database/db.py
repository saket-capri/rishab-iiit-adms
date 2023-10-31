from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config
# SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:db2325Rish@bh@localhost:3306/attendance"
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://attendance"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

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