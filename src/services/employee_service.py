import csv
from typing import List, Optional, Dict
from datetime import datetime
import os

# Helper function to get the next available ID
def get_next_id() -> int:
    if not os.path.exists("data/employee_data.csv"):
        return 1  # Start with 1 if the file does not exist
    with open("data/employee_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        ids = [int(row["employee_id"]) for row in reader if row["employee_id"].isdigit()]
    return max(ids, default=0) + 1

def get_employees() -> List[Dict[str, str]]:
    employees = []
    with open("data/employee_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append({
                "employee_id": row["employee_id"],
                "first_name": row["first_name"],
                "surname": row["surname"],
                "department": row["department"],
                "position": row["position"],
                "start_date": row.get("start_date", ""),
                "end_date": row.get("end_date", "")
            })
    return employees

def get_employee(employee_id: str) -> Optional[Dict[str, str]]:
    with open("data/employee_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["employee_id"] == employee_id:
                return row
    return None

def add_employee(employee: Dict[str, str]) -> Dict[str, str]:
    employee_id = str(get_next_id())
    with open("data/employee_data.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee_id] + [employee.get(field, "") for field in ["first_name", "surname", "department", "position", "start_date", "end_date"]])
    return {"employee_id": employee_id}

def update_employee(employee_id: str, updated_employee: Dict[str, str]) -> bool:
    rows = []
    with open("data/employee_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["employee_id"] == employee_id:
                rows.append({**row, **updated_employee})
            else:
                rows.append(row)
    
    with open("data/employee_data.csv", mode="w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return True

def delete_employee(employee_id: str) -> bool:
    rows = []
    with open("data/employee_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["employee_id"] != employee_id:
                rows.append(row)
    
    with open("data/employee_data.csv", mode="w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return True



def get_avg_salary(employee_id: str) -> Dict[str, float]:
    department = None

    # Find the department of the given employee
    with open("data/employee_data.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["employee_id"] == employee_id:
                department = row.get("department", "").strip()  # Use .get() to avoid KeyError
                break

    if not department:
        return {"message": f"Employee with ID {employee_id} not found or department missing"}

    total_salary = 0
    employee_count = 0
    
    # Calculate the average salary for the department
    with open("data/employee_salaries.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        print(f"Headers in employee_salaries.csv: {headers}")  # Debugging line
        
        for row in reader:
            row_department = row.get("department", "").strip()  # Use .get() to avoid KeyError
            salary_str = row.get("salary", "").strip()
            if row_department == department and salary_str:
                try:
                    total_salary += float(salary_str)
                    employee_count += 1
                except ValueError:
                    print(f"Invalid salary format: {salary_str}")  # Debugging line

    if employee_count == 0:
        return {"avg_salary": 0.0}

    avg_salary = total_salary / employee_count
    return {"avg_salary": avg_salary}

        # department = None
        
        # # First, find the department of the given employee
        # with open("data/employee_data.csv", newline='') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for row in reader:
        #         if row["employee_id"] == employee_id:
        #             department = row["department"]  # Ensure this matches the CSV header
        #             break

        # if not department:
        #     raise ValueError(f"Employee with ID {employee_id} not found")

        # total_salary = 0
        # employee_count = 0
        
        # # Check headers in the salaries file
        # with open("data/employee_salaries.csv", newline='') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     headers = reader.fieldnames
        #     print(f"Headers in employee_salaries.csv: {headers}")  # Debugging line
            
        #     for row in reader:
        #         if row.get("department") == department:  # Use get() to avoid KeyError
        #             total_salary += float(row.get("salary", 0))  # Default to 0 if salary is missing
        #             employee_count += 1

        # if employee_count == 0:
        #     return {"avg_salary": 0.0}

        # avg_salary = total_salary / employee_count
        # return {"avg_salary": avg_salary}

    
def get_months_of_service(employee_id: str) -> Dict[str, int]:
    employee = get_employee(employee_id)
    if not employee:
        return {"message": "Employee not found"}
    
    start_date_str = employee.get("start_date", "").strip()
    if not start_date_str:
        return {"message": "Start date is missing or empty"}
    
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    except ValueError:
        return {"message": "Invalid start date format"}
    
    end_date_str = employee.get("end_date", "").strip()
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d") if end_date_str else datetime.now()

    months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    return {"months": months}

def get_years_of_service(employee_id: str) -> Dict[str, int]:
    employee = get_employee(employee_id)
    if not employee:
        return {"message": "Employee not found"}
    
    start_date_str = employee.get("start_date", "").strip()
    if not start_date_str:
        return {"message": "Start date is missing or empty"}
    
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    except ValueError:
        return {"message": "Invalid start date format"}
    
    end_date_str = employee.get("end_date", "").strip()
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d") if end_date_str else datetime.now()

    years = end_date.year - start_date.year - ((end_date.month, end_date.day) < (start_date.month, start_date.day))
    return {"years": years}

