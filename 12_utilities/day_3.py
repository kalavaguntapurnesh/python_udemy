
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


num_people = int(input("How Many people are there in the group ? "))

names = []

for i in range(num_people):
    name = input(f"Enter the name of person {i + 1} : ") # i starts from 0, so we add 1 to display the correct person number
    names.append(name)
    

total_bill = get_float("Enter the bill amount in number only ")

share = round(total_bill / num_people, 2)

print("\n "  + "*" * 40)
print(f"Total bill : {total_bill}")
print(f"Each person owes {share}")


for name in names:
    print(f"{name} owes {share}")

print("*" * 40)