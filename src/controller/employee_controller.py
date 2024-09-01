from fastapi import APIRouter, HTTPException
from src.schemas.employee_schemas import Employee
from src.services.employee_service import (
    get_employees,
    get_employee,
    add_employee,
    update_employee,
    delete_employee,
    get_avg_salary,
    get_months_of_service,
    get_years_of_service
)

router = APIRouter()

@router.get("/employees")
def get_all_employees():
    return get_employees()

@router.get("/employees/{employee_id}")
def read_employee(employee_id: str):
    employee = get_employee(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.post("/employees")
def create_employee(employee: Employee):
    return add_employee(employee)

@router.put("/employees/{employee_id}")
def modify_employee(employee_id: str, employee: Employee):
    updated = update_employee(employee_id, employee)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee updated"}

@router.delete("/employees/{employee_id}")
def remove_employee(employee_id: str):
    deleted = delete_employee(employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted"}

@router.get("/employees/{employee_id}/avg-salary")
def average_salary(employee_id: str):
    return get_avg_salary(employee_id)

@router.get("/employees/{employee_id}/months-of-service")
def months_service(employee_id: str):
    return get_months_of_service(employee_id)

@router.get("/employees/{employee_id}/years-of-service")
def years_service(employee_id: str):
    return get_years_of_service(employee_id)
