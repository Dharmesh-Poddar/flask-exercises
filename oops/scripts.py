class Parrot:

	species= "Bird"

	def __init__(self,name,age):
		self.name= name
		self.age= age


Dodo= Parrot("dodo",13)
Togo= Parrot("togo",12)
print("dodo is a {}".format(Dodo.__class__.species))
print("togo is a {}".format(Togo.__class__.species))


print("{} is {} years old".format(Dodo.name,Dodo.age))
print("{} is {} years old".format(Togo.name,Togo.age))