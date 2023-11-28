from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship
from database.db import Base, engine
from student_model import StudentInfo
class SemesterInfo(Base):
    __tablename__ = "semester_table"

    id = Column(Integer, primary_key=True)
    semester_no = Column(Integer, nullable=False)

    student_table = relationship("StudentInfo", back_populates = "semesterInfo")
