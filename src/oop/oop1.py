# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Parrent Class
class Vehicle:
    pass

# Child Class
class GroundVehicle(Vehicle):
    pass

# Grandchild class
class Car(GroundVehicle):
    pass

# Grandchild Class
class Motorcycle(GroundVehicle):
    pass

# Child Class
class FlightVehicle(Vehicle):
    pass

# Grandchild class
class Starship(FlightVehicle):
    pass

# Grandchild class
class Airplane(FlightVehicle):
    pass