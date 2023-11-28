from typing import List
from fastapi import FastAPI
from sqlalchemy.orm import Session
from Exception.exceptions import StudentInfoInfoAlreadyExistError, StudentInfoNotFoundError, WrongPhoneNumberError, WrongEmailError
from models.student_model import StudentInfo
from schema.schemas import CreateAndUpdateStudent

# Function to get list of student info
def get_all_students(session: Session, limit: int, offset: int) -> List[StudentInfo]:
    return session.query(StudentInfo).offset(offset).limit(limit).all()


# Function to  get info of a particular student
def get_student_info_by_id(session: Session, student_roll_no: int) -> StudentInfo:
    student_info = session.query(StudentInfo).get(student_roll_no)

    if student_info is None:
        raise StudentInfoNotFoundError
        
        # print("StudentInfoNotFoundError")
    
    return student_info
# @app.post('/add_new', response_model=CreateAndUpdateStudent)
def create_student(session: Session,student_info: CreateAndUpdateStudent) -> StudentInfo:
    student_details = session.query(StudentInfo).filter(StudentInfo.first_name ==student_info.first_name, StudentInfo.last_name == student_info.last_name).first()
    if student_details is not None:
        raise StudentInfoInfoAlreadyExistError
    
    new_student_info = StudentInfo(**student_info.dict())
    session.add(new_student_info)
    session.commit()
    session.refresh(new_student_info)
    return new_student_info

# Function to update details of the student
def update_student_info(session: Session, _id: int, info_update: CreateAndUpdateStudent) -> StudentInfo:
    student_info = get_student_info_by_id(session, _id)

    if student_info is None:
        raise StudentInfoNotFoundError

    student_info.first_name = info_update.first_name
    student_info.last_name = info_update.last_name
    student_info.phone = info_update.phone
    student_info.semester = info_update.semester
    student_info.email = info_update.email
    
    session.commit()
    session.refresh(student_info)

    return student_info


# Function to delete a student info from the db
def delete_student_info(session: Session, _id: int):
    student_info = get_student_info_by_id(session, _id)

    if student_info is None:
        raise StudentInfoNotFoundError

    session.delete(student_info)
    session.commit()

    return