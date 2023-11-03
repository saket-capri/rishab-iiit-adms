# models.py

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from db import Base, engine
# from database.config import MySQLdb
class StudentInfo(Base):
    __tablename__ = "student_table"

    student_roll_no = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    lastname= Column(String)
    email = Column(String, nullable=False)
    phone = Column(String)
    semester = Column(Integer, nullable=False)
    # Base.metadata.create_all(bind=engine)


