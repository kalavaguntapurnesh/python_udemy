class Chai:
    temperature = "hot"
    strength = "strong"


cutting = Chai()
print(cutting.temperature)  # Output: hot

cutting.temperature = "cold"
print(cutting.temperature)  # Output: cold

print(Chai.temperature)  # Output: hot

cutting.cup = "Small"

print(cutting.cup)  # Output: Small

del cutting.temperature
print(cutting.temperature)  # Output: hot got back to class attribute