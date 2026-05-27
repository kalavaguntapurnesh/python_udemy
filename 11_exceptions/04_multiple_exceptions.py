def process_order(item, quantity):
    try:
        price = {"masala" : 20}[item]
        cost = price * quantity
        print(f"Total cost for {quantity} {item}(s) is: {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be a number")
    
    
process_order("masala", 2)  # Valid order
process_order("chai", 2)     # Invalid item
process_order("masala", "two")  # Invalid quantity