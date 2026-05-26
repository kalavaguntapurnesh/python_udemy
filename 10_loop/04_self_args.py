class Chaicup:
    size = 150
    
    def describe(self): #describe method takes self as an argument
        return f"A {self.size}ml cup of tea."
    

cup = Chaicup()
print(cup.describe()) # This will print "A 150ml cup of tea." because the describe method is called on an instance of the Chaicup class, and self refers to that instance.
print(Chaicup.describe()) # This will raise an error because describe is an instance method and requires an instance (self) to be passed as an argument.


cup_two = Chaicup()
cup_two.size = 200
print(cup_two.describe()) # This will also print "A 150ml cup of tea." because cup_two is another instance of the Chaicup class, and self refers to that instance as well.

