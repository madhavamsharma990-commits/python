class BMW:
    def fuel_type(self):
        print("BMW uses Diesel/Petrol")
    def max_speed(self):
        print("Max speed is 240 mph")
class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Premium Petrol")
    def max_speed(self):
        print("Max speed is 350 mph")
def car_details(car_object):
    print("Car Details:")
    car_object.fuel_type()
    car_object.max_speed()
    print("-" * 20)
car1 = BMW()
car2 = Ferrari()
car_details(car1)
car_details(car2)
print("Iterating over car objects:")
for car in (car1, car2):
    car.fuel_type()
    car.max_speed()
    print("-" * 20)
