def chai_flavour(flavour = "masala"):
    
    """Return the flavour of chai. Default is masala."""
    
    return flavour

print(chai_flavour.__doc__)
print(chai_flavour.__name__)


help(len)

def generate_bill(chai=0, samosa=0):
    """calculate teh total
    bill for chai and samosa
    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosas (20 rupees each)
    :return: Total bill amount

    """
    total = chai * 10 + samosa * 20
    return total, "Thank you for visiting chaicode.com"
    
    