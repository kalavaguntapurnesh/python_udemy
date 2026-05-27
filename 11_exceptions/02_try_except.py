chai_menu = {
    "masala" : 30,
    "ginger" : 25,
    "cardamom" : 35,
}

print(chai_menu["masala"])  # Output: 30


# chai_menu["elaichi"]  # This will raise a KeyError since "elaichi" is not in the chai_menu dictionary


try:
    chai_menu["elaichi"]  # This will raise a KeyError
except KeyError:
    print("The key 'elaichi' does not exist in the chai_menu dictionary.")

