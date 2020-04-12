class Vehicle: 

	numVehicles = 0

	def __init__(self, color, weight, numDoors, topSpeed, currentSpeed):
		self.color = color
		self.weight = weight
		self.numDoors = numDoors
		self.topSpeed = topSpeed
		self.currentSpeed = currentSpeed
		self.__class__.numVehicles += 1
