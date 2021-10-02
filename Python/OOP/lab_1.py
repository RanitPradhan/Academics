class Vehicle:
    def __init__(self,no_of_wheels,engine_capacity,seating_capacity,max_velocity):
        self.no_of_wheels=no_of_wheels
        self.engine_capacity=engine_capacity
        self.seating_capacity=seating_capacity
        self.max_velocity=max_velocity
    
BMW_model=Vehicle(8,'inline-six',9,500)
print("Number of wheels: ",BMW_model.no_of_wheels)
print("Engine Capacity: ",BMW_model.engine_capacity)
print("Seating Capacity: ",BMW_model.seating_capacity)
print("Maximum Velocity: ",BMW_model.max_velocity)
