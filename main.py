# main.py
# Import FastAPI
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import uvicorn
import models
from db import SessionLocal, engine, Base, get_db
from crud import get_all_students, create_student, get_student_info_by_id, update_student_info, delete_student_info
from schemas import Student, CreateAndUpdateStudent, PaginatedStudentInfo
from exception import StudentInfoException
# Initialize the app
app = FastAPI()

# Base.metadata.create_all(bind=engine)

session: Session = Depends(get_db)

              

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to Attendance Management System"}


# API to get the list of student info
@app.get("/students", response_model=PaginatedStudentInfo)
def list_students(session: Session = Depends(get_db), limit: int = 10, offset: int = 0):
    students_list = get_all_students(session, limit, offset)

    response = {"limit": limit, 
                "offset": offset, 
                "data": students_list
    }

    return response


# API endpoint to add a student info to the database
@app.post("/students")
def add_student(student_info: CreateAndUpdateStudent, session: Session = Depends(get_db)):
        try:
            new_student = create_student(session, student_info)
            return new_student
        except StudentInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular student
@app.get("/students/{student_id}", response_model=Student)
def get_student_info(student_id: int, session: Session = Depends(get_db)):
    try:
        student_info = get_student_info_by_id(session, student_id)
        return student_info
    except StudentInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API to update a existing student info
@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, new_info: CreateAndUpdateStudent, session: Session = Depends(get_db)):

    try:
        student_info = update_student_info(session, student_id, new_info)
        return student_info
    except StudentInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a student info from the data base
@app.delete("/students/{student_id}")
def delete_student(student_id: int, session: Session = Depends(get_db)):

    try:
        return delete_student_info(session, student_id)
    except StudentInfoException as cie:
        raise HTTPException(**cie.__dict__)