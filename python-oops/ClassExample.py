class Car:
	def _init_(self, name, year, enginePower):
		self.name = name
		self.year = year
		self.enginePower = enginePower
	
	def getName(self):
		return self.name
	
	def getYear(self):
		return self.year
	
	def getPower(self):
		return string(enginePower) + ' HP'
		
myAudi = Car("Audi", 2020, 100)
print(myAudi)
