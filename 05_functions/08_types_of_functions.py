def pure_chai(cups):
    return cups * 10

print(pure_chai(5)) # will return 50 because the function multiplies the input by 10 and returns the result.




# not recommended to use global variables as it can lead to unexpected behavior and makes the code harder to debug and maintain.
def impure_chai(cups):
    global total_cups
    total_cups += cups * 10
    print(total_cups)

total_cups = 0
impure_chai(5)
    
    
chai_types = ["light", "dark", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))

weak_chai = list(filter(lambda chai : chai != "kadak", chai_types))


print(strong_chai) # will return ['kadak'] because the filter function is used to filter out the elements in the chai_types list that are equal to "kadak".

print(weak_chai) # will return ['light', 'dark', 'ginger'] because the filter function is used to filter out the elements in the chai_types list that are not equal to "kadak".