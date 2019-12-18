from basic import db, puppy


##create##
my_puppy= puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()


##Read ##

all_puppies =puppy.query.all()
print(all_puppies)

##select by id

puppy_one =puppy.query.get(1)
print(puppy_one.name)

#filters

puppy_frankie = puppy.query.filter_by(name='Rufus')
print(puppy_frankie.all())

#update

secondpup= puppy.query.get(2)
secondpup.age=20
db.session.add(secondpup)
db.session.commit()
print(secondpup)

##delete
della=puppy.query.get(1)
db.session.delete(della)
db.session.commit()



##printing all

all_puppues=puppy.query.all()
print(all_puppues)



