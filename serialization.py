from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

u = User(name="Pratik", age=19)
print(u.model_dump())

