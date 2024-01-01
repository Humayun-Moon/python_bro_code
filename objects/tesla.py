from car import Car
class Tesla(Car):
    def __init__(self, name, model, price,aName, atribute):
        super().__init__(name, model, price,)
        self.aName = aName        
        self.atribute = atribute

    def modeTesla (self):
        print(f"The Car name is {self.name} and model number is to {self.model}. If you would like to buy it have to needed {self.price}") 
        print(f"We have another collection {self.aName} and it a {self.atribute} car you can drive it comfortably")
      

