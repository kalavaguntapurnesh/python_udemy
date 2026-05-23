numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)

evens = [x for x in numbers if x % 2 == 0]
print(evens)

odds = [x for x in numbers if x % 2 != 0]
print(odds)

names = ["Alice", "Bob", "Charlie", "David"]
upper_names = [name.upper() for name in names]
print(upper_names)