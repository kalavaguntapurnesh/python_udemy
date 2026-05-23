class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(1, 2)
v2 = Vector(3, 5)

result = v1 + v2
print(result) # Output: Vector(4, 7)



class Student:
    def __init__(self, marks):
        self.marks = marks
    
    def __eq__(self, other):
        return self.marks == other.marks
    
s1 = Student(90)
s2 = Student(90)

print(s1 == s2) # Output: True

