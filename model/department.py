from sqlmodel import Relationship, SQLModel, Field


class Department(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str
    employees: list["Employee"] = Relationship(back_populates="deparment")
