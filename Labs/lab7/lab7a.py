#!/usr/bin/env python3

# Store one IPv4 address
class IPAddress:
    # You probably want to construct it as a string, but you may want to store it as the four octets separately:
	def __init__(self, address):
		self.address = address
        
    # Is this address from a private subnet? e.g. starting with 192.168. or 10.
	def isPrivate(self):
		if (self.address[:7])  == "192.168":
			private = "private"
			return private
		elif self.address[:2] == "10":
			private = "private"
			return private
		else:
			public = "public"
			return public
# Store information about a person, perhaps someone you'll be adding as a user to a system:
class Person:
	def __init__(self, role, name, age, gender):
		self.role
		self.name = name
		self.age = age
		self.gender
	

# Store information about different models from a specific manufacturer. Perhaps how many seats they have and how much fuel they use and the price range:
# Doesn't have to be BMW, pick any car or bike manufacturer:
class BMWModel:

	def __init__(self, model, seats, fueltype, price, color):
		self.model = model
		self.seats = seats
		self.fueltype = fueltype
		self.price = price
		self.color = color
    	

# Store information about a specific car that someone owns.
# Spend some time thinking why this class is different than the one above, and whether it has to be different:
class Car:

	def __init__(self, owner, car, color, vin):
		self.owner = owner
		self.car = car
		self.color = color
		self.vin = vin
		
