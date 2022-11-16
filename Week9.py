print("1)")
class Vehicle:
    def __init__(car, make, model):
        car.make = make
        car.model = model
vehicle_1 = Vehicle("Ford","Mustang")
vehicle_2 = Vehicle("Toyota","Camry")
print(vehicle_1.make)
print(vehicle_2.model)

print("\n2")
vehicle_3 = Vehicle("Maserati","Levante")
vehicle_4 = Vehicle("Porsche","944")
print(vehicle_3.__init__)
print("\n3")