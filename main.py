from fastapi import FastAPI
from src.controller import employee_controller, department_controller

app = FastAPI()

app.include_router(employee_controller.router)
app.include_router(department_controller.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Employee Management System"}




if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
