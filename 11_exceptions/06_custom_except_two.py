class OutOfIngredientsError(Exception):
    
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Not enough ingredients to make chai.")
    print("Chai is ready!")
    
make_chai(1, 1)
print("Trying to make chai with insufficient ingredients...")
make_chai(0, 1)