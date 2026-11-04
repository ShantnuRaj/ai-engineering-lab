from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    

def insert_patient_data(patient: Patient):


    print(patient.name)
    print(patient.age)
    print('inserted')


def update_patient_data(patient: Patient):


    print(patient.name)
    print(patient.age)
    print('updated')


patient_info = {'name': 'Shantnu','age':21, 'weight': 69.6, 'married':False, 'allergies':['pollen', 'dust'], 'contact_details': 'rshantnu626@gmail.com', 'phone':'8298425655'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
    