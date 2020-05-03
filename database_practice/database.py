from app import db,Rajasthan
db.create_all()

nagaur= Rajasthan(21,nagaur)
chittor= Rajasthan(2, chittor)

db.session.add_all([nagaur, chittor])
db.session.commit()

print(nagaur.id)

print(chittor.id)
