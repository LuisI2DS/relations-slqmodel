from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from db.db import get_session
from model.department import Department
from model.employee import Employee, EmployeeCreate

router = APIRouter(prefix="/employee", tags=["Employee"])


@router.get("/")
def all_employees(db: Session = Depends(get_session)):
    employees = db.exec(select(Employee)).all()
    return employees


@router.post("/")
def create_employee(
    # employee: EmployeeCreate,
    db: Session = Depends(get_session),
):
    marketing = Department(name="TI")

    new_employee = Employee(name="Uriel", email="u@u.com", deparment=marketing)

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee
