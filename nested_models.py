from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Patient(BaseModel):
    name: str
    age: int
    address: Address

patient1 = Patient(
    name="Pratik",
    age=19,
    address=Address(city="Sangli", state="Maharashtra", pincode=416312)
)
print(patient1)