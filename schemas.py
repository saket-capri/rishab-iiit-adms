# schemas.py
from pydantic import BaseModel
from typing import List


# TO support creation and update APIs
class CreateAndUpdateStudent(BaseModel):
    first_name: str
    last_name: str
    semester: int
    email: str
    phone: str


# TO support list and get APIs
class Student(CreateAndUpdateStudent):
    student_roll_no: int

    class Config:
        from_attributes = True


# To support list cars API
class PaginatedStudentInfo(BaseModel):
    limit: int
    offset: int
    data: List[Student]

