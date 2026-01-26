class vehicle :
    def __init__(self,mileage, max_speed):
     self.max_speed = max_speed
     self.mileage = mileage
modelx = vehicle(200,18)
print("Model X Speed:", modelx.max_speed, "Mileage:", modelx.mileage)