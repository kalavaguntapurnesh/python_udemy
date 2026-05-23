essential_spices = {"cardamom", "ginger", "cinnamon", "cloves"}
optional_spices = {"cloves", "ginger", "nutmeg", "saffron"}

essential_spices.__contains__("cardamom")

# Find the spices that are in both sets
common_spices = essential_spices.intersection(optional_spices)

print(common_spices)

# Find the spices that are in either set
either_spices = essential_spices.union(optional_spices)

print(either_spices)

# Find the spices that are in essential_spices but not in optional_spices
unique_essential_spices = essential_spices.difference(optional_spices)

print(unique_essential_spices)

# Find the spices that are in optional_spices but not in essential_spices
unique_optional_spices = optional_spices.difference(essential_spices)

print(unique_optional_spices)