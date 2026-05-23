chai_type = "Ginger chai"

customer_name = "Purnesh"

print(f"Order for {customer_name} : {chai_type} please!")


chai_description = "Aromatic and Bold"
print(f"First Word is : {chai_description[0:8:1]}")
print(f"Two Word is : {chai_description[0:8:2]}")
print(f"Three Word is : {chai_description[8:]}")
print(f"Reverse Word is : {chai_description[::-1]}")

label_text = "Chai Special"

encoded_label = label_text.encode("utf-8")

print(f"Encoded Label : {encoded_label}")
