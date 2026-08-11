from pydantic import BaseModel


class Student(BaseModel):
    Gender: str
    Age: float
    City: str
    Profession: str
    Academic_Pressure: float
    Work_Pressure: float
    CGPA: float
    Study_Satisfaction: float
    Job_Satisfaction: float
    Sleep_Duration: str
    Dietary_Habits: str
    Degree: str
    Suicidal_Thoughts: str
    Work_Study_Hours: float
    Financial_Stress: float
    Family_History_of_Mental_Illness: str