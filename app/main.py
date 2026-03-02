import dataclasses
from datetime import datetime
import pickle

@dataclasses.dataclass
class Speciality:
    name : str
    number : int

@dataclasses.dataclass
class Student:
    first_name : str
    last_name : str
    birth_date : datetime
    average_mark : float
    has_scholarship : bool
    phone_number : str
    address  : str


@dataclasses.dataclass
class Group:
    speciality : Speciality
    course : int
    students : list[Student]

def write_groups_information(groups_list):
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups_list, f)
        
    counts = []
    for group in groups_list:
        counts.append(len(group.students))
        
    return max(counts) if counts else 0


def write_students_information(students):
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)

def read_groups_information():
    with open("groups.pickle", "rb") as f:
        groups_list = pickle.load(f)
    
    unique_specialties = set()
    for group in groups_list:
        unique_specialties.add(group.speciality.name)

    return unique_specialties

def read_students_information():
    with open("students.pickle", "rb") as f:
        students_list = pickle.load(f)

    return students_list
