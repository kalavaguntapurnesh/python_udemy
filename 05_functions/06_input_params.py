chai = "Ginger Tea"

def prepare_chai(order):
    print(f"Preparing {order}")


prepare_chai(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


make_chai("Ginger Tea", "Full Cream", "2 spoons")

def special_chai(*inngredients, **extras):
    print("Ingredients:", inngredients)
    print("Extras:", extras)

special_chai("Cinnamon", "Cardamom", sweetner = "Honey", foam = "Yes")