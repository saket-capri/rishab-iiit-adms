from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database.db import Base, engine
# from database.config import MySQLdb
class SubjectInfo(Base):
    __tablename__ = "subject_table"

    subject_id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String, nullable=False)
    semester= Column(Integer, nullable=False)
    # Base.metadata.create_all(bind=engine)