from pydantic import BaseModel, AnyUrl, EmailStr, computed_field
from typing import List, Dict
# instead of using list or dict we are using the typing module List/Dict because we want to do 2 level validation(allergies is list but each item inside is a string).

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin: AnyUrl
    height: float
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    # to compute a new field value from existing model properties, this value is not provided by user. we use this decorator
    # we get instance of our pydantic model as input "self"
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('bmi', patient.bmi)
     
patient_info = {'name':'john', 'linkedin':'http://linkedin.com' ,'email':'ab@hdfc.com', 'age': '65', 'height':1.72, 'weight': 78.6, 'married': True, 'contact_details': {'email': 'abc@gmail.com', 'emergency':'2344323'}, 'allergies': ['pollen', 'dust']}
patient1 = Patient(**patient_info) #once value is passed to model it perform first validation -> then type coercion and build a pydantic model
insert_patient_data(patient1)
temp = patient1.model_dump()
print(temp)
temp1 = patient1.model_dump_json()
print(temp1)