class parret:
    species = "bird"
    def __init__(self, name,age):
        self.name = name
        self.age = age
blu = parret("Blu",10)
woo = parret("Woo",15)
print(blu.species)
print(woo.species)
print(blu.name)
print(woo.name)
print(blu.age)
print(woo.age)