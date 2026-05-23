ingredients = ["water", "milk", "black tea"]

print(f"Ingredients: {ingredients}")

ingredients.append("sugar")
print(f"Ingredients after adding sugar: {ingredients}")

ingredients.remove("water")
print(f"Ingredients after removing water: {ingredients}")

spice_options = ["cardamom", "ginger"]

ingredients.extend(spice_options)

print(f"Ingredients after adding spices: {ingredients}")

spice_options.insert(1, "badam")

print(f"Spice Options after adding badam: {spice_options}")

spice_options.remove("cardamom")
print(f"Spice Options after removing cardamom: {spice_options}")


spice_options.reverse()
print(f"Spice Options after reversing: {spice_options}")

spice_options.sort()
print(f"Spice Options after sorting: {spice_options}")


sugar_levels = [1, 2, 3, 4, 5]

print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")


base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour

print(f"Full Liquid Mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3

print(f"Strong Brew: {strong_brew}")


from operator import itemgetter


