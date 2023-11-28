# main.py
# Import FastAPI
from fastapi import FastAPI, APIRouter, status,Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
import uvicorn
import models.student_model as models
from database.db import SessionLocal, engine, Base, get_db
from crud import get_all_students, create_student, get_student_info_by_id, update_student_info, delete_student_info
from schema.schemas import Student, CreateAndUpdateStudent, PaginatedStudentInfo
from Exception.exceptions import StudentInfoException
# from Exceptions.jwt_exceptions import *
from jose import jwt, JWTError
from Auth.jwt_based import *
# from Auth.token_based import *


session: Session = Depends(get_db)

# from new_main import router

app = FastAPI()


@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]

# @app.post("/token")
# async def login(
#     form_data: OAuth2PasswordRequestForm = Depends(),
#     db: Session = Depends(get_db),
# ):
#     user = authenticate_user(form_data.username, form_data.password, db)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     return {"access_token": user.username, "token_type": "bearer"}

# @app.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user

# GET operation at route '/'
@app.get('/')
def root_api():

    return {"message": "Welcome to Attendance Management System"}


# API to get the list of student info
@app.get("/students", response_model=PaginatedStudentInfo)
def list_students(current_user: User = Depends(get_current_active_user),
                  session: Session = Depends(get_db), 
                  limit: int = 10, offset: int = 0):
    
        students_list = get_all_students(session, limit, offset)
        response = {"limit": limit, 
                    "offset": offset, 
                    "data": students_list
        }
        return response


# API endpoint to add a student info to the database
@app.post("/students")
def add_student(student_info: CreateAndUpdateStudent, 
                session: Session = Depends(get_db)):
    
    try:
        new_student = create_student(session, student_info)
        return new_student
    except StudentInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular student
@app.get("/students/{student_id}", response_model=Student)
def get_student_info(student_id: int, 
                     session: Session = Depends(get_db)):
    try:
        student_info = get_student_info_by_id(session, student_id)
        return student_info
    except StudentInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API to update a existing student info
@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, 
                   new_info: CreateAndUpdateStudent, 
                   session: Session = Depends(get_db)):
    try:
        student_info = update_student_info(session, student_id, new_info)
        return student_info
    except StudentInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a student info from the data base
@app.delete("/students/{student_id}")
def delete_student(student_id: int, 
                   session: Session = Depends(get_db)):
    try:
        return delete_student_info(session, student_id)
    except StudentInfoException as cie:
        raise HTTPException(**cie.__dict__)

