from pydantic import BaseModel
from typing import List

# Define a schema for a department
class DepartmentBase(BaseModel):
    name: str

# Define a schema for the list of all departments
class DepartmentList(BaseModel):
    departments: List[str]

# Define a schema for an employee within a department
class DepartmentEmployee(BaseModel):
    employee_id: int
    first_name: str
    surname: str
    department: str
    position: str

# Define a schema for the list of employees in a department
class DepartmentEmployeesList(BaseModel):
    employees: List[DepartmentEmployee]
