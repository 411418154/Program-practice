from dataclasses import dataclass , field
from typing import List

@dataclass
class Student:
    scores : List[float] = field(default_factory=list)

s1 = Student()
print(s1.scores)   # []
s1.scores.append(90)
print(s1.scores)   # [90]
s1.scores.append(100)
print(s1.scores)

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Frame:
    points: List[Point] = field(default_factory=list)

s2 = Frame()
s2.points.append(Point(1.22 , 1.44))
s2.points.append(Point(5.66, 7.88))
print(s2.points)