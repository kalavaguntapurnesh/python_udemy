def local_chai():
    
    yield "Masala Chai"
    yield "Ginger Chai"
    
def imported_chai():
    yield "Matcha"
    yield "Oolong"
    
def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order..."
    except GeneratorExit:
        print("Chai stall is closing...")
        
stall = chai_stall()
print(next(stall))  # Start the generator and get the initial message
print(stall.send("Masala Chai"))  # Send an order and get the waiting message
stall.close()  # Close the generator to trigger the GeneratorExit exception