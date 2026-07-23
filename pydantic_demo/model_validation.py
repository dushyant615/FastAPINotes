from pydantic import BaseModel, AnyUrl, EmailStr, model_validator
from typing import List, Dict
# instead of using list or dict we are using the typing module List/Dict because we want to do 2 level validation(allergies is list but each item inside is a string).

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin: AnyUrl
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    # to perform data validation on multiple field combined we use model_validator decorator
    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have an emergency contact')
        return model
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
     
patient_info = {'name':'john', 'linkedin':'http://linkedin.com' ,'email':'ab@hdfc.com', 'age': '65', 'weight': 78.6, 'married': True, 'contact_details': {'email': 'abc@gmail.com', 'emergency':'2344323'}, 'allergies': ['pollen', 'dust']}
patient1 = Patient(**patient_info) #once value is passed to model it perform validation -> then type coercion.
insert_patient_data(patient1)