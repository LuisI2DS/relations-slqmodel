from sqlmodel import Relationship, SQLModel, Field

from model.department import Department


class Employee(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str
    email: str
    deparment_id: int = Field(default=None, foreign_key="department.id")

    deparment: Department = Relationship(back_populates="employees")


class EmployeeCreate(SQLModel):
    name: str
    email: str
