def make_chai():
    print("Here is your masala chai!")

return_value = make_chai()

print(return_value) # will return "None" because the function does not have a return statement.


def idle_chaiwala():
    pass

print(idle_chaiwala()) # will also return "None" because the function does not have a return statement.


def sold_cups():
    return 120

total = sold_cups()
print(total) # will return 120 because the function has a return statement that returns the value 120.



def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is available"
    print("chai")

print(chai_status(0))
print(chai_status(5))
    


def chai_report():
    return 100, 20 # sold, remaining

sold, remaining = chai_report()
print(f"Sold: {sold}, Remaining: {remaining}")