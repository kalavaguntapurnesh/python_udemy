class ChaiOrder:
    
    type = None
    def __init__(self, type_, size):
        self.type = type_ #type is a reserved keyword in python, so we use type_ instead
        self.size = size #size is in ml
    
    def summary(self):
        return f"{self.size} ml of {self.type} chai"

order = ChaiOrder("Masala", 250)
print(order.summary())

order_two = ChaiOrder("Ginger", 300)
print(order_two.summary())