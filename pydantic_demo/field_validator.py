from pydantic import BaseModel, AnyUrl, EmailStr, Field, field_validator
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

    # to perform datavalidation on single field we use field validation decorator
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    # field validator gets value in two modes i.e after/before type coercion. default is after. 
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be between 0 to 100')

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
     
patient_info = {'name':'john', 'linkedin':'http://linkedin.com' ,'email':'ab@hdfc.com', 'age': '30', 'weight': 78.6, 'married': True, 'contact_details': {'email': 'abc@gmail.com', 'phone':'2344323'}, 'allergies': ['pollen', 'dust']}
patient1 = Patient(**patient_info) #once value is passed to model it perform validation -> then type coercion.
insert_patient_data(patient1)