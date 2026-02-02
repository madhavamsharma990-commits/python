class bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} is flying!"
    def sing(self):
        return f"{self.name} is singing!"
class penguin(bird):
    def fly(self):
        return f"{self.name} cannot fly."
    def swim(self):
        return f"{self.name} is swimming!"
    def __init__(self, name):
        super().__init__(name)
        print(f"Penguin {self.name} created.") 
object = penguin("Pingu")
print(object.fly())
print(object.sing())
print(object.swim())