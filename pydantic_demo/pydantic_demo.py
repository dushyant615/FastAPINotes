from pydantic import BaseModel, AnyUrl, EmailStr, Field
from typing import List, Dict, Optional, Annotated
# instead of using list or dict we are using the typing module List/Dict because we want to do 2 level validation(allergies is list but each item inside is a string).

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50,title='Name of Patient', description='Give the name of patient in less the 50 char', examples='Nitish,John')]
    age: int = Field(gt=0, lt=120, strict=True)
    email: EmailStr
    linkedin: AnyUrl
    weight: float = Field(gt=0, strict=True)
    married: bool = False
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
    contact_details: Dict[str,str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
     
patient_info = {'name':'john', 'linkedin':'http://linkedin.com' ,'email':'ab@gmail.com', 'age': 30, 'weight': 78.6, 'contact_details': {'email': 'abc@gmail.com', 'phone':'2344323'}, 'allergies': ['pollen', 'dust']}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)