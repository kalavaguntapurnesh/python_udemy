def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "cardamom", "saffron"]:
        raise ValueError(f"Sorry, we don't have {flavor} chai.")
    return f"Here's your {flavor} chai!"

print(brew_chai("masala"))  # This will work fine
print(brew_chai("chocolate"))  # This will raise a ValueError


