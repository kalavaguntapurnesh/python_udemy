def chai_customer():
    print("Welcome ! What chai would you like ?")
    
    order = yield
    print(f"Great choice ! Your {order} will be ready soon.")
    while True:
        print(f"Preparing: {order}...")
        order = yield
        print(f"Great choice ! Your {order} will be ready soon.")
        
customer = chai_customer()
next(customer)  # Start the generator

customer.send("Masala Chai")
customer.send("Ginger Chai")