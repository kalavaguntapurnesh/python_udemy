is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling  # This is called "UPCASTING"

print(f"Total Actions: {total_actions}")

# milk_present = "Purnesh"

milk_present = None
print(f"Is There Milk : {bool(milk_present)}")


water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can Serve Chai: {can_serve}")

import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.499999999999

print(f"Ideal Temp {ideal_temp}")
print(f"Current Temp {current_temp}")
print(f"Difference Temp {ideal_temp - current_temp}")
print(sys.float_info)
# print(decimal)