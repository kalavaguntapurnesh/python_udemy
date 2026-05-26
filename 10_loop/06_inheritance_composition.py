class BaseChai:
    
    def __init__(self, type_):
        self.type = type_ #_ is used to avoid conflict with the built-in type function
    
    def prepare(self):
        print(f"Preparing {self.type} chai...")
    
class MasalaChai(BaseChai):
    
    def add_spices(self):
        print("Adding cardamom, ginger, cloves to the chai...")
    

class ChaiShop:
    
    chai_cls = BaseChai
    
    def __init__(self):
        self.chai = self.chai_cls("Regular")
        
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop..")
        self.chai.prepare()
        

class FancyChaiShop(ChaiShop):
    
    chai_cls = MasalaChai
    

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai_cls.add_spices("Gingering")
fancy.chai.add_spices()
   


    
    