
##  Incompleted ##
class Polygon:
	__width=None
	__height = None

def set_value(self,width,height):
	self.__width= width
	self.__height= height

def get_width(self):
	return self.__width

def get_height(self):
	return self.__height

class Square(Polygon):
	def area(self):
		return self.get_width()* self.get_height()

s1= Square()
s1.set_value(8,15)
print(s1.area())

class Triangle(Polygon):
	def area(self):
		return self.get_width()* self.get_height()*1/2

s1=Square()
s1.set_value(8,15)
print(s1.area())

t1= Triangle()
t1.set_value(5,10)
print(t1.area())


class Rectangle(Polygon):
	def area(self):
		return self.get_width()* self.get_height()

s1=Square()
s1.set_value(8,15)
print(s1.area())

r1= Rectangle()
r1.set_value(2,3)
print(r1.area())

class Hexagon(Polygon):
	def area(self):
		return 2.6*self.get_width()^2 

s1=Square()
s1.set_value(8,15)
print(s1.area())

p1= Hexagon()
p1.set_value(10,15)
print(p1.area())