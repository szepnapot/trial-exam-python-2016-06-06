# Create a class that represents a cuboid:
# It should take it's three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class GeometryCalc:

	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def getSurface(self):
		return 'Surface: {}'.format(2*(self.a * self.b + self.a * self.c + self.c * self.b))

	def getVolume(self):
		return 'Volume: {}'.format(self.a * self.b * self.c)


g = GeometryCalc(5, 3, 5)
print(g.getSurface())
print(g.getVolume())