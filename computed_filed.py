from pydantic import BaseModel,computed_field


class Patient(BaseModel):
    weight:float
    height:float
    
    @computed_field
    @property
    def BMI(self)->float:
        return round(self.weight/(self.height**2),2)
    
person=Patient(weight=70,height=1.75)
print(person.BMI)