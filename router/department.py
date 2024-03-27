from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from db.db import get_session
from model.department import Department
from model.employee import Employee

router = APIRouter(prefix="/deparment", tags=["Deparment"])


@router.get("/")
def all_deparments(db: Session = Depends(get_session)):
    deparments = db.exec(select(Department)).all()
    return deparments


@router.post("/")
def create_deparment(db: Session = Depends(get_session)):
    new_employee = Employee(name="Naka", email="naka@naka@.com")

    finance = Department(name="Finanzas", employees=[new_employee])

    db.add(finance)
    db.commit()
    db.refresh(finance)
    return finance
