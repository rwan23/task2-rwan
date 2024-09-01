# from pydantic import BaseModel
# from typing import Optional

# class Employee(BaseModel):
#     first_name: str
#     surname: str
#     email: str
#     date_of_birth: str
#     department: str
#     position: str
#     start_date: int
#     end_date: Optional[int] = None


from pydantic import BaseModel
from datetime import date

class Employee(BaseModel):
    first_name: str
    surname: str
    email: str
    date_of_birth: date
    department: str
    position: str
    start_date: date
    end_date: date
