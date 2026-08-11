from pydantic import BaseModel

class Student(BaseModel):
    program: str
    level: str
    age: int