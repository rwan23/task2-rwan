from fastapi import APIRouter, HTTPException
from src.services.department_service import get_departments, get_department_employees

router = APIRouter()

@router.get("/departments")
def list_departments():
    return get_departments()

@router.get("/departments/{department_name}/employees")
def department_employees(department_name: str):
    employees = get_department_employees(department_name)
    if not employees:
        raise HTTPException(status_code=404, detail="Department not found")
    return employees
