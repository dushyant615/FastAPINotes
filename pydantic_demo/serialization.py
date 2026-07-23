from pydantic import BaseModel

# Pydantic takes the raw dict and:
# 1.Validates the types (age must be an int).
# 2.Converts compatible values ("30" → 30).
# 3.Raises errors if the data doesn’t match.

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str ='male'
    age: int
    address: Address

address_dict = {'city':'nagpur', 'state': 'maharashtra', 'pin':'441324'}
address1 = Address(**address_dict)

patient_dict ={'name':'john', 'age':35, 'address': address1}
patient1 = Patient(**patient_dict)

# to export data model into dict or json format we use this methods
temp = patient1.model_dump()
print(temp)
print(type(temp))
temp1 = patient1.model_dump_json()
print(temp1)
print(type(temp1))
temp2 = patient1.model_dump(include=['name','gender'])
print(temp2)
print(type(temp2))
temp3 = patient1.model_dump(exclude={'address':['state']})
print(temp3)
print(type(temp3))
temp3 = patient1.model_dump(exclude_unset=True)
print(temp3)
print(type(temp3))