class Showroom:
    def __init__(self, name , add):
        self.name = name
        self.add = add
    def info (self):
        print(f"The {self.name} at {self.add} ")   
# s = Showroom("Humayun", "Moon")              
# s.info()