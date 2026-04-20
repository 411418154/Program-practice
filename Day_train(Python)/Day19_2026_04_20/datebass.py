from dataclasses import dataclass

@dataclass
class Student:
    name : str
    age : int

s1 = Student("Amy", 20)
print(s1.name)
print(s1.age)
print(s1)

class room:
    def __init__(self,names,age):
        self.names = names
        self.age = age

s2 = room("Tom",19)
print(s2.names)
print(s2.age)
print(s2)
