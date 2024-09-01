import csv

def get_departments() -> list[str]:
    departments = set()
    with open("data/employee_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            departments.add(row["department"])
    return list(departments)

def get_department_employees(department_name: str) -> list[dict]:
    employees = []
    with open("data/employee_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["department"] == department_name:
                employees.append({
                    "employee_id": row["employee_id"],
                    "first_name": row["first_name"],
                    "surname": row["surname"],
                    "department": row["department"],
                    "position": row["position"]
                })
    return employees
