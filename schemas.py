# schemas.py
from pydantic import BaseModel
from typing import List


# TO support creation and update APIs
class CreateAndUpdateStudent(BaseModel):
    id:int
    student_roll_no: int
    first_name: str
    last_name: str
    semester: int
    email: str
    phone: str
    class Config:
        from_attributes = True


# TO support list and get APIs
class Student(CreateAndUpdateStudent):
    id:int

    class Config:
        orm_mode = True


# To support list cars API
class PaginatedStudentInfo(BaseModel):
    limit: int
    offset: int
    data: List[Student]

