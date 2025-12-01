
from pydantic import BaseModel,EmailStr,AnyUrl,field_validator
from pydantic import Field
from typing import List,Dict,Optional

class Patient(BaseModel):
    email:EmailStr
    @field_validator("email")
    def check_gmail(cls,value):
        if not value.endswith("@gmail.com"):
            raise ValueError("only gmail address")
        return value

    
def insert_patient_data(patient:Patient):
    print(patient.email)
    


patient_info={'email':'pratik@gmail.com',}

patient1=Patient(**patient_info)

insert_patient_data(patient1)

