square_dict = {x : x * x for x in range(10)}
print(square_dict)

students = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78
}

passed = {name : marks for name, marks in students.items() if marks >= 80}
print(passed)   