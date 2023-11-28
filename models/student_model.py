# models.py

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database.db import Base, engine
# from database.config import MySQLdb
class StudentInfo(Base):
    __tablename__ = "student_table"

    id = Column(Integer, primary_key=True, index = True)
    student_roll_no = Column(Integer, unique=True)
    first_name = Column(String, nullable=False)
    last_name= Column(String)
    email = Column(String, nullable=False)
    phone = Column(String)
    semester = Column(Integer, nullable=False)
    # Base.metadata.create_all(bind=engine)
    # method creates the corresponding tables in the database.


