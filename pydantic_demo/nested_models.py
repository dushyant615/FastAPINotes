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
    gender: str
    age: int
    address: Address

address_dict = {'city':'nagpur', 'state': 'maharashtra', 'pin':'441324'}
address1 = Address(**address_dict)

patient_dict ={'name':'john', 'gender':'m', 'age':35, 'address': address1}
patient1 = Patient(**patient_dict)

print(patient1.address.city)