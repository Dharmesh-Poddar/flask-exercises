class Person:
	def __init__(self,name,age):
		self.name= name
		self.age = age


#    def Mobile(self,mobile):
 #       return "{} has {} phone".format(self.name,mobile)


	def sing(self,song):
	    return "{} is singing {} ".format(self.name, song)

    

Rohan = Person("rohan",20)

print(Rohan.sing("despacito"))
#print(Rohan.Mobile("iphone6"))

