
class StudentInfoException(Exception):
    def __init__(self):
        self.status_code = 400

class StudentInfoNotFoundError(StudentInfoException):
    def __init__(self):
        # self.status_code = 404
        self.detail = "Student Info Not Found"
        print("StudentInfoNotFoundError")

class StudentInfoInfoAlreadyExistError(StudentInfoException):
    def __init__(self):
        # self.status_code = 409
        self.detail = "Student Info Already Exists"

class WrongPhoneNumberError(StudentInfoException):
    def __init__(self):
        # self.status_code = 410
        self.detail = "Wrong Phone Number Entered"
    
class WrongEmailError(StudentInfoException):
    def __init__(self):
        # self.status_code = 411
        self.detail = "Wrong Email Entered"