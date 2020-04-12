class Vehicle: 
	def __init__(self, make, model, color, weight, numDoors, topSpeed, currentSpeed):
		self.make = make 
		self.model = model 
 		self.color = color
		self.weight = weight
		self.numDoors = numDoors
		self.topSpeed = topSpeed
		self.currentSpeed = currentSpeed

	def accelerate(self):
		if self.currentSpeed < self.topSpeed:
			self.currentSpeed = self.currentSpeed + 5
		return self.currentSpeed

  	def brake(self):
		if self.currentSpeed > 0:
			self.currentSpeed = self.currentSpeed - 5
		if self.currentSpeed < 5:
			self.currentSpeed = 0
		return self.currentSpeed

markCar = Vehicle("Nissan", "Rogue", "Silver", 4200, 5, 110, 0)
momCar = Vehicle("Hyundai", "Tucson", "Aqua", 3900, 5, 120, 0)

#print(markCar.make + " " + markCar.model)
#print(momCar.make + " " + momCar.model)

#markCar.currentSpeed = 50
#markCar.color = "black"
#print("Speed: " + str(markCar.currentSpeed))
markCar.accelerate()
markCar.accelerate()
print("The vehicle is now moving at " + str(markCar.currentSpeed) + " MPH.")
