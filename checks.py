import re
# class checking():
def check_phone(phone: str):
        if len(phone) != 10:
            return False
        elif len(phone) == 10:
            for i in range(10):
                if phone[i] >'9' or phone[i] <'0':
                    return False
        else:
            return True
        
def check_email(email):
    # Defining a regular expression pattern for a valid email address
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Using the re.match() function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False