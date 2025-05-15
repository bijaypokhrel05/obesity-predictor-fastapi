from pydantic import BaseModel

class Person(BaseModel):
    height: float
    weight: float
