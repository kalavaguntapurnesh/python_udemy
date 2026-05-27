class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {"masala" : 20, "ginger"  : 15, "cardamom" : 25}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"Sorry, we don't have {flavor} chai.")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer.")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai is: {total} rupees.")
    except:
        print("An error occurred while processing your order. Please try again.")
    finally:
        print("Thank you for visiting our chai shop!")
    
# Example usage:
bill("masala", 2)  # Valid order
bill("vanilla", 2)  # Invalid flavor