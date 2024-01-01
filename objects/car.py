class Car :
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price


    def run (self):
        print("Below the info of car It can Run from here")
        print(f"The Car name is {self.name} and model number is to {self.model}. If you would like to buy it have to needed {self.price}") 
    def stop(self):
        print("The car can stop within neno second")


# t =Tesla("Volvo", "hk2000", " $ 2 core ", "Tesla", "Electronics")
# t.modeTesla()