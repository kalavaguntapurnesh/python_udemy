class Chai:
    origin = "india"
    name = "Purnesh"

print(Chai.origin)
print(Chai.name)

Chai.is_hot = True
print(Chai.is_hot)

# Creating objects from class Chai

masala = Chai()

print(masala.origin)
print(masala.name)
print(masala.is_hot)

masala.is_hot = False

print(masala.is_hot)
print(Chai.is_hot)

masala.flavour = "Spicy"
print(masala.flavour)
print(Chai.flavour)  # This will raise an error as flavour is not defined in class Chai