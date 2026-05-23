masala_spices = ("cardamom", "cinnamon", "clove")
print(masala_spices)

(spice1, spice2, spice3) = masala_spices

print(f"Main Masala Spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1

print(f"Ratio is G : {ginger_ratio} and C : {cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

print(f"After swapping, Ratio is G : {ginger_ratio} and C : {cardamom_ratio}")


# Membership 

print(f"Is cardamom in masala spices? {'cardamom' in masala_spices}")
print(f"Is pepper in masala spices ? {'pepper' in masala_spices}")