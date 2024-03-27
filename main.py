from fastapi import FastAPI
from model import department, employee
from router import employee, department
from db.db import init_db

init_db()

app = FastAPI()

app.include_router(employee.router)
app.include_router(department.router)


@app.get("/")
def root():
    return {"message": "run run"}
