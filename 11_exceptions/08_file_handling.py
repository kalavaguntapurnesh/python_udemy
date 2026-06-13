# file = open("order.txt", "w")

# try:
#     file.write("Masala Chai - 2 Cups")
# finally:
#     file.close()



with open("order.txt", "w") as file:
    file.write("Ginger Chai - 2 Cups")