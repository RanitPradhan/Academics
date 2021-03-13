
class vehicle():
    def __init__ (self):
        print("Vehicle")

class LandVehicle(vehicle):
    def __init__ (self):
        vehicle.__init__(self)
        print("landvehicle")

class car(LandVehicle):
    def __init__(self):
        LandVehicle.__init__(self)
        print("Four wheels")
        print("car")

class twheels(LandVehicle):
    def __init__(self):
        LandVehicle.__init__(self)
        print("Two wheels")

class bicycle(twheels):
    def __init__(self):
        twheels.__init__(self)
        print("---------")
        print("Bicycle")

class motorcycle(twheels):
    def __init__(self):
        print("----------")
        super().__init__()
        print("Motor cycle")

class watervehicle(vehicle):
    def __init__(self):
        vehicle.__init__(self)
        print("Water vehicle")
        
class airvehicle(vehicle):
    def __init__(self):
        vehicle.__init__(self)
        print("Air vehicle")

class powered(airvehicle):
    def __init__(self):
        airvehicle.__init__(self)
        print("Powered")

class unpowered(airvehicle):
    def __init__(self):
        airvehicle.__init__(self)
        print("Unpowered")

class propeller(powered):
    def __init__(self):
        print("-----------")
        powered.__init__(self)
        print("Propeller")

class jet(powered):
    def __init__(self):
        print("----------")
        powered.__init__(self)
        print("Jet")
        
x=motorcycle()
a=jet()
print(propeller.__mro__)