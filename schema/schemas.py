# schemas.py
from pydantic import BaseModel, constr, validator
from typing import List
from Exception.exceptions import WrongEmailError, WrongPhoneNumberError
import re


# TO support creation and update APIs
class CreateAndUpdateStudent(BaseModel):
    id:int
    student_roll_no: int
    first_name: str
    last_name: str
    semester: int
    email: constr(min_length=2)
    phone: constr(min_length=10, max_length=10)

    @validator("email")
    def check_email(cls,value):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        # Using the re.match() function to check if the email matches the pattern
        if re.match(pattern, value) is False:
            raise ValueError("Email entered in incorrect")
        
        return value
            
        
    @validator("phone")
    def check_phone(cls, value):
        for i in range(10):
            if value[i] >'9' or value[i] <'0':
                raise ValueError("Phone number must contain only digits")
        return value
    # class Config:
    #     from_attributes = True


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

