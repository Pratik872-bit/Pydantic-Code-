
from pydantic import BaseModel,EmailStr,AnyUrl,field_validator
from pydantic import Field
from typing import List,Dict,Optional

class Patient(BaseModel):
    
    name :str
    age :int 
    weight:float=Field(gt=0, lt=120)
    linkedin_url:AnyUrl
    email:EmailStr
    married:Optional[bool]=None
    allergies:list[str]
    contactz_details:dict[str,str]
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.linkedin_url)
    print(patient.email)
    print(patient.married)
    print(patient.allergies)
    print(patient.contactz_details)
    print('inserted')


patient_info={'name':'pratik','age':19,'weight':45.34,'linkedin_url':'https://chatgpt.com/c/692d18b8-a5e0-8320-9b79-b6cc4e8cf5e1','email':'pratik@gmail.com','married':True,'allergies':['pratik'],'contactz_details':{'phone':'8788417313'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)

