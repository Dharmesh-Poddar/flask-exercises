class Person:
	def __init__(self,name,age):
		self.name= name
		self.age = age



	def sing(self,song):
	    return "{} is {} years old".format(self.name, song)

    def mobile(self,mobile):
        return "{} has {} phone".format(self.name, mobile)


Rohan = Person(rohan,20)

print(Rohan.sing("despacito"))
print(Rohan.mobile("iphone6"))

